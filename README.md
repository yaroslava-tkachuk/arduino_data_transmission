# arduino_data_transmission
Arduino USB data transmission project.

A simple application created to test USB data transfer process between Arduino and PC using Python and C++. It represents the work of two 8-bit registers functioning in U2 system and basic processor operations done on them.

Author: Yaroslava Tkachuk, BSc student of the University of Silesia, Katowice, Poland.

Files

Python application:
- main_alu.py - main program loop
- alu_simulator.py - GUI
- serial_bus.py - contains data transfer class
- hex_bytes.py - pretty ugly workaround doing bitwise operations on numbers of a fixed length using Python strings (numpy could be a prettier option, but this one is hand made and created with love)
- limited_string_var.py - catching and fixing all kinds of user weirdness from the GUI level

Arduino application:
- ard_serial_bus.ino - main program loop
- b_alu_simulator_class.ino - contains ALU simulator class that performs operations on data received from the PC

Additional files:
- alu_background.png - fancy background picture taken from https://pixabay.com/de/illustrations/atx2-microcontroller-arduino-950511/ (thank You, guys who left it there)

Hardware:
- Arduino Uno R3
- USB cable
- PC

Workflow:
1) User provides 1 or 2 numbers in range [-128, 127] and picks an operation to be performed on them.
2) Data is formatted and an input packet is created.
3) Packet is transferred to Arduino by USB.
4) Arduino receives and checks packet: validation byte and control sum (bitwise XOR of all bytes).
5) If the packet is valid, the operation is performed on data.
6) Operation output is formatted and an output packet is created.
7) The packet is sent back to the PC.
8) PC receives the output packet and validates it.
9) If the packet is valid, the data is formatted into decimal numbers and operation output as well as the carry are displayed.

Operations supported:
- addition
- subtraction
- AND
- OR
- XOR
- NOT
- bitwise left and right one byte shifts

Packet structure

Header [2 bytes]:
- validation byte - 10101010 which increases the probability of an error in case of data transfer problems and hence contributes to the system safety [1 byte]
- number of bytes in body [1 byte]

Body [4-6 bytes]:
- operation code [1 byte]
- A input [2 bytes]
- B input [2 bytes]
- control sum [1 byte]

What can be improved:
1) Adding constant verification of the devices' availability.
2) Making error messages more generic.

If You want to play around with the code, please, make sure that:
1) Your Arduino is connected to the PC.
2) Arduino code is burned onto Your board (Arduino Studio or any similar software can be used).
3) You have checked the port to which Arduino is connected and correct value of _arduino_port attribute is set in serial_bus.py file.

You can run the program from terminal by navigating to its directory and running the following command:
python3 main_alu.py

Have fun!
