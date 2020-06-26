#include<Arduino.h>
#ifndef alu_simulator_class
#define alu_simulator_class


class ALUSimulator
//Gets and processes serial bus data
{
  public:
  
    int two_bytes_into_int(byte high, byte low)
    //Converts 2 bytes into a 2-byte int
    {
      int converted;
      
      converted = high;                //high -> rightmost 8 bits
      converted = converted << 8;      //high -> leftmost 8 bits
      converted |= low;                //low -> rightmost 8 bits
      
      return converted;
    }
    
    void process_data()
    //Performs opcode operation on a and b operands
    {
      int a;
      int b;
      int res;
      
      a = this->get_a();
      b = this->get_b();
      
      switch(this->get_opcode())
      {
        case 0:
          res = a + b;
          break;
        case 1:
          res = a - b;
          break;
        case 2:
          res = a & b;
          break;
        case 3:
          res = a | b;
          break;
        case 4:
          res = a ^ b;
          break;
        case 5:
          res = ~ a;
          break;
        case 6:
          res = a >> 1;
          break;
        case 7:
          res = a << 1;
          break;
        }
        this->set_result(res);
      }

      bool get_new_data()
      //1) Gets opcode, a, and b opeands as hex bytes
      //2) Coverts them into 2-byte ints
      //3) Updatees opcode, a, and b attributes
      {
        if(Serial.available() >= 8)
        {
          byte rec_packet_start;
          byte rec_num_of_bytes;
          
          byte rec_opcode;
          byte rec_a_high;
          byte rec_a_low;
          byte rec_b_high;
          byte rec_b_low;
          
          byte rec_contr_sum;
          
          int new_packet_start;
          int new_num_of_bytes;
          
          int new_opcode;
          int new_a;
          int new_b;
          
          byte calculated_contr_sum;
          
          //Get packet start and compare it with own packet start
          rec_packet_start = Serial.read();
          new_packet_start = rec_packet_start;
          
          if (rec_packet_start == this->get_packet_start())
          {
            //Get data
            rec_num_of_bytes = Serial.read();
            new_num_of_bytes = rec_num_of_bytes;
            
            rec_opcode = Serial.read();
            new_opcode = rec_opcode;
            
            rec_a_high = Serial.read();
            rec_a_low = Serial.read();
            
            if (new_num_of_bytes == 6)
            {            
              rec_b_high = Serial.read();
              rec_b_low = Serial.read();
            }
            
            rec_contr_sum = Serial.read();
            
            //Calculate control sum and compare it with received control sum
            if (new_num_of_bytes == 6)
            {  
              calculated_contr_sum = rec_packet_start ^ rec_num_of_bytes ^ rec_opcode ^ rec_a_high ^ rec_a_low ^ rec_b_high ^ rec_b_low;
            }
            else if (new_num_of_bytes == 4)
            {
              calculated_contr_sum = rec_packet_start ^ rec_num_of_bytes ^ rec_opcode ^ rec_a_high ^ rec_a_low;
            }
            
            if (calculated_contr_sum == rec_contr_sum)
            {
              //Convert operans to 2-byte ints and update attributes
              //Convert
              new_a = this->two_bytes_into_int(rec_a_high, rec_a_low);
              new_b = this->two_bytes_into_int(rec_b_high, rec_b_low);
              //Update
              this->set_a(new_a);
              this->set_b(new_b);
              this->set_opcode(new_opcode);
              return true;
            }
          }
        }
        return false;
      }
      
      void update_data(int new_opcode, int new_a, int new_b)
      //Updates all attributes with new data
      {
        this->set_opcode(new_opcode);
        this->set_a(new_a);
        this->set_b(new_b);
      }      
      
      void send_result()
      //Sends result back to PC as a low and high byte of int
      {
        int res;
        res = this->get_result();
        
        Serial.write(highByte(res));
        Serial.write(lowByte(res));
      }
      
      void handle_requests()
      //Gets data from PC and sends result of the operation
      {
          if (this->get_new_data())
          {
            this->process_data();
            this->send_result();
          }
      }

      //Getters
      int get_a()
      {
        return this->a;  
      }

      int get_b()
      {
        return this->b;  
      }

      int get_opcode()
      {
        return this->opcode;  
      }

      int get_result()
      {
        return this->result;  
      }
      
      int get_packet_start()
      {
        return this->packet_start;  
      }

      //Setters
      void set_a(int new_a)
      {
        this->a = new_a;  
      }

      void set_b(int new_b)
      {
        this->b = new_b;  
      }

      void set_opcode(int new_opcode)
      {
        this->opcode = new_opcode;  
      }

      void set_result(int new_result)
      {
        this->result = new_result;  
      }
      
      void set_packet_start(int new_packet_start)
      {
        this->packet_start = new_packet_start;  
      }

  private:
    int a;
    int b;
    int opcode;
    int result;
    int packet_start = 170;
};

#endif
