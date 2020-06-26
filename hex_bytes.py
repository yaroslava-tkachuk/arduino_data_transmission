import binascii
from functools import reduce


class HexByte():

	'''Handles bin and hex string conversions and XOR operation.'''

	def __init__(self):
		self._hex_bin = {
			'0': '0000', '1': '0001', '2': '0010', '3': '0011',
			'4': '0100', '5': '0101', '6': '0110', '7': '0111',
			'8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
			'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'
			}
		self._bin_hex = dict(zip(self.hex_bin.values(), self.hex_bin.keys()))

	@property
	def hex_bin(self):
		return self._hex_bin

	@property
	def bin_hex(self):
		return self._bin_hex

	def bytes_to_str(self, bytes_val):

		'''Converts bytes object into a list of strings.

		IN: bytes object
		OUT: list of 2-char strings corresponding to each hex halves of
		a byte.'''
		
		hex_str = str(binascii.b2a_hex(bytes_val))[2:-1]
		hex_str_list = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
		return hex_str_list

	def hex_to_bin(self, hex_byte_str):
		'''Converts a given hex byte string into bin byte string.'''
		bin_byte = self.hex_bin[hex_byte_str[0]] +\
				   self.hex_bin[hex_byte_str[1]]
		return bin_byte

	def hexes_to_bins(self, hex_bytes_str):
		
		'''Converts a given list of hex byte strings into bin byte
		strings.'''
		
		bin_bytes = [self.hex_to_bin(b) for b in hex_bytes_str]
		return bin_bytes

	def bin_xor(self, bin_bytes_1, bin_bytes_2):
		
		'''Performs a bitwise XOR on a string representation of
		bytes.'''
		
		result = ''
		for i in range(len(bin_bytes_1)):
			if bin_bytes_1[i] == bin_bytes_2[i]:
				result += '0'
			else:
				result += '1'
		return result

	def bin_to_hex(self, bin_byte_str):
		'''Converts a given bin byte string into hex byte string.'''
		hex_byte = self.bin_hex[bin_byte_str[0:4]] +\
				   self.bin_hex[bin_byte_str[4:]]
		return hex_byte

	def str_to_bytes(self, hex_str):
		'''Converts hex string into bytes object.'''
		return binascii.a2b_hex(hex_str)

	def hex_xor(self, bytes_val):

		'''Performs bitwise XOR on all bytes of a hex bytes object.

		IN: hex bytes object
		OUT: hex bytes object which is a XOR of all given bytes'''

		# Convert hex bytes object into list of bin strings
		hex_str = self.bytes_to_str(bytes_val)
		bin_strs = self.hexes_to_bins(hex_str)
		
		# Perform XOR on list of bin strings
		bin_xor_res = reduce((lambda x, y: self.bin_xor(x, y)), bin_strs)

		# Convert list of bin strings back to hex bytes object
		hex_str_res = self.bin_to_hex(bin_xor_res)
		hex_xor_res = self.str_to_bytes(hex_str_res)

		return hex_xor_res