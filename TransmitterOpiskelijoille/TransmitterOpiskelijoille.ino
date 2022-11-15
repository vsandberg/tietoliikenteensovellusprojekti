#include "messaging.h"
#include "accelerator.h"


// 1 = X + ylös
// 2 = X - alas

// 3 = Y + ylös
// 4 = Y - alas

// 5 = Z + ylös
// 6 = Z - alas



void setup()
{
  Serial.begin(9600);
  // Kiihtvyys-anturin napojen määrittely:
  const int GNDPin2 = A4;  // laitteen maa-napa
  const int VccPin2 = A0;  // Käyttöjännite

  pinMode(VccPin2, OUTPUT);     // Kiihtyvyysanturin käyttöjännite Vcc
  pinMode(GNDPin2, OUTPUT);     // Kiihtyvyysanturin GND



  // Asetetaan syöttöjännite
  digitalWrite(VccPin2, HIGH);
  delayMicroseconds(2);
  digitalWrite(GNDPin2, LOW);
  delayMicroseconds(2);

}

void loop()
{
  Accelerator Aobject;
  Messaging Mobject;

  Serial.println("Give arduino rotation // 1 - 6");
  int RotationDirection = 0;
  
  
  
  while (RotationDirection == 0)
  {
    if (Serial.available() > 0)
    {
      RotationDirection = Serial.parseInt();

    }
  }
  
  Serial.println("Give number how many measurements");
  int NumberOfMeasurements = 0;
  
  
  
  while (NumberOfMeasurements == 0)
  {
    if (Serial.available() > 0)
    {
      NumberOfMeasurements = Serial.parseInt();

    }
  }
  
  
 

  for (int M = 0; M < NumberOfMeasurements; M++)
  {
    
    Aobject.makeMeasurement();
    Measurement m = Aobject.getMeasurement();
    Aobject.tulostus();
    uint8_t id = M;
    uint8_t flags = RotationDirection;
    Mobject.createMessage(m);
    if (Mobject.sendMessage(id, flags))
    {
      Serial.println("Successfull transmission");
     
    }
    else
    {
      Serial.println("Transmission fails");
      Serial.println("Successfull transmission");
      
    }
    if (Mobject.receiveACK())
    {
      Serial.println("Receiver got message, going to next measurement");
      
    }
    else
    {
      Serial.println("Receiver did not get the message. Need to resend it");
      
      M--;  // Let's just rewind for loop
    }
  } // end of for
}   // end of loop
