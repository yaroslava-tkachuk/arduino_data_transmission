import serial
from serial.tools import list_ports
import struct

from hex_bytes import HexByte

class SerialBus():

	'''Sends data to Arduino, receives and formats the output.'''

	def __init__(self):
		self._arduino_port = '/dev/ttyACM0'
		# Solution for Windows
		# self._arduino_port = self.find_Arduino(self.get_ports())
		self._serial_bus = serial.Serial(self.arduino_port,	baudrate=9600,
										timeout=1)
		self._packet_start = 170 #10101010 in binary

	#Getters
	@property
	def arduino_port(self):
		return self._arduino_port

	@property
	def serial_bus(self):
		return self._serial_bus

	@property
	def packet_start(self):
		return self._packet_start

	#Setters
	@arduino_port.setter
	def arduino_port(self, new_arduino_port):
		self._arduino_port = new_arduino_port

	@serial_bus.setter
	def serial_bus(self, new_serial_bus):
		self._serial_bus = new_serial_bus

	@packet_start.setter
	def packet_start(self, new_packet_start):
		self._packet_start = new_packet_start

	def get_ports(self):
		
		'''Gets port - device list of all devices connected to the PC.

		Workd with Windows OS only.'''

		return list_ports.comports()

	def find_Arduino(self, ports_found):
		'''Finds port to which Arduino is connected.'''
		arduino_port = None
		for port in ports_found:
			if 'Arduino' in str(port):
				arduino_port = str(port).split(' ')[0]
		return arduino_port

	def data_to_bytes(self, opcode, a, b):
		'''Converts given data into bytes.'''
		if b is not None:
			packet = struct.pack('>BBBhh', self.packet_start, 6, opcode, a, b)
		else:
			packet = struct.pack('>BBBh', self.packet_start, 4,	opcode, a)
		return packet

	def calc_control_sum(self, packet):
		'''Calculates control sum as a bitwise XOR of all given data.'''
		hex_byte = HexByte()
		contr_sum = hex_byte.hex_xor(packet)
		return contr_sum	

	def prepare_data(self, opcode, a, b):
		'''Creates a packet of bytes and appends a control sum to it.'''
		packet = self.data_to_bytes(opcode, a, b)
		contr_sum = self.calc_control_sum(packet)
		packet += contr_sum
		return packet

	def send_data(self, opcode, a, b):
		
		'''Sends user input data as a bytes packet to Arduino.
		
		IN: int a, int b, int opcode
		
		SENT: packet_start/number_of_bytes/opcode/a_high/a_low/b_high/
			  b_low/control_sum [8B]
		or packet_start/number_of_bytes/opcode/a_high/a_low/
		   control_sum [6B]'''

		packet = self.prepare_data(opcode, a, b)
		self.serial_bus.write(packet)

	def receive_data(self):
		
		'''Receives result data from Arduino.
		
		Receives result packet, formats, checks start and control sum.
		RECEIVED: packet_start/result_high/result_low/control_sum'''
		
		result = None
		rec_packet = self.serial_bus.read(size=4)
		if len(rec_packet) > 0:
			rec_contr_sum = rec_packet[-1].to_bytes(1, 'big')
			packet_start, output = struct.unpack('>Bh', rec_packet[:-1])
			if packet_start == self.packet_start:
				contr_sum = self.calc_control_sum(rec_packet[:-1])
				if rec_contr_sum == contr_sum:
					result = output
		return result

	def perform_operation(self, opcode, a, b):

		'''Sends formatted user data to Arduino and gets the output.

		IN: int opcode in [0, 7], int a, b in [-128, 127]
		OUT: int taking up to 2 bytes'''

		self.send_data(opcode, a, b)
		output = self.receive_data()
		return output

	def format_output(self, output):

		'''Formats output.

		IN: int taking up to 2 bytes
		OUT: int in [-128, 127], carry in [0, 1]'''
		
		carry = 0
		formatted_output = output
		if output > 127:
			formatted_output = output % 127
			carry = 1
		elif output < -128:
			formatted_output = output % -128
		return formatted_output, carry