#include "accelerator.h"
#include <arduino.h>

Accelerator::Accelerator()
{
  Serial.println("Accelerator created!");
}


Accelerator::~Accelerator()
{
  Serial.println("Accelerator deleted!");
}



void Accelerator::makeMeasurement()
{
  m.x = analogRead(xPin);
  m.y = analogRead(yPin);
  m.z = analogRead(zPin);
}

Measurement Accelerator::getMeasurement()
{
  return m;
}

void Accelerator::tulostus()
{
  Serial.println(m.x);
  Serial.println(m.y);
  Serial.println(m.z);
}
