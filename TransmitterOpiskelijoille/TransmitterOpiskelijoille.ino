#include "messaging.h"
#include "accelerator.h"
#include "keskipisteet.h"

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
  float value;
  int i;
  int j;
  int location;
  
  
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
  
  
 

  for (int M = 0; M < NumberOfMeasurements;)
  {
    
    Aobject.makeMeasurement();
    Measurement m = Aobject.getMeasurement();
    Aobject.tulostus();
    uint8_t id = M;
    uint8_t flags = RotationDirection;
    Mobject.createMessage(m);
    float minvalue = 500;
    for (int j = 0; j < 6;)
    {
                value = abs(sqrt(pow((w[j][0]- m.x),2) +             
                                pow((w[j][1]- m.y),2) +        
                                pow((w[j][2]- m.z),2)));
                //Serial.println(value);
                

       
          if (value < minvalue)
          {
            minvalue = value;
            location = w[j][3];
          }
          
           j++;     
    }//end for j
  Serial.print(RotationDirection);
  Serial.print(",");
  Serial.println(location);
    
    
    M++;  // Let's just rewind for loop
  } // end of for
}   // end of loop
