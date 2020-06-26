//#include<Arduino.h>
#include "b_alu_simulator_class.ino"

  
ALUSimulator ALU;
  
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  ALU.handle_requests();  
}
