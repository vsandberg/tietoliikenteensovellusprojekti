#ifndef ACCELERATOR_H
#define ACCELERATOR_H

#include "messaging.h"

struct Measurement
{
  int x;
  int y;
  int z;
};

class Accelerator
{
  public:
    Accelerator();
    ~Accelerator();
    void tulostus();
    void makeMeasurement();
    Measurement getMeasurement();
   
    

  private:
    Measurement m;
     
    // Määritellään kytkentänavat kiihtyvyysanturille:
    const int xPin   = A1;   // x-kanavan mittaus
    const int yPin   = A2;   // y-kanava
    const int zPin   = A3;   // z-kanava
  
};

#endif // ACCELERATOR_H
