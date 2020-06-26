from tkinter import StringVar


class LimitedStringVar(StringVar):

	'''StringVar with restricted value to handle user input.'''

	def __init__(self):
		super().__init__()
		self._max_length = 4
		self._max_val = 127
		self._min_val = -128
		self.trace('w', self.limit)

	#Getters
	@property
	def max_length(self):
		return self._max_length

	@property
	def max_val(self):
		return self._max_val

	@property
	def min_val(self):
		return self._min_val
	
	#Setters
	@max_length.setter
	def max_length(self, new_max_length):
		self._max_length = new_max_length

	@max_val.setter
	def max_val(self, new_max_val):
		self._max_val = new_max_val

	@min_val.setter
	def min_val(self, new_min_val):
		self._min_val = new_min_val

	#Restrict user input length
	def limit_length_neg(self):
		
		"""Truncates characters of a negative number that exceed
		max_length."""
		
		val = self.get()
		if len(val) > self.max_length:
				self.set(val[:self.max_length])

	def limit_length_pos(self):
		
		"""Truncates characters of a positive number that exceed
		max_length - 1."""
		
		val = self.get()
		if len(val) > self.max_length - 1:
				self.set(val[:self.max_length-1])

	def limit_length(self, var, indx, mode):
		'''Truncates characters that exceed the length limit.'''
		val = self.get()
		if self.is_negative(val):
			self.limit_length_neg()
		else:
			self.limit_length_pos()

	#Restrict user input characters type
	def is_negative(self, val):
		"""Cehcks if number is negative."""
		if val[0] == '-':
			return True
		else:
			return False

	def trunc_not_numbers(self, val):
		"""Truncates all characters that are not numbers."""
		return ''.join([ch for ch in val if ch.isnumeric()])

	def limit_char_type_neg(self):
		
		'''Truncates characters that are not numbers, except minus at
		the beginning.'''
		
		val = self.get()
		changed_val = False
		if (len(val) > 1 and not val[1:].isnumeric()):
			self.set('-'+self.trunc_not_numbers(val[1:]))
			changed_val = True
		return changed_val

	def limit_char_type_pos(self):
		'''Truncates all characters that are not numbers.'''
		val = self.get()
		changed_val = False
		if not val.isnumeric():
			self.set(self.trunc_not_numbers(val))
			changed_val = True
		return changed_val

	def limit_char_type(self, var, indx, mode):
		'''Truncates characters that are not numbers.'''
		val = self.get()
		changed_val = False
		if self.is_negative(val):
			changed_val = self.limit_char_type_neg()
		else:
			changed_val = self.limit_char_type_pos()
		return changed_val

	#Restrict user input value
	def string_to_int(self, val):
		"""Converts string value to int."""
		int_val = 0
		if ((self.is_negative(val) and len(val) > 1) or
			not self.is_negative(val)):
				int_val = int(val)
		return int_val

	def limit_value(self, var, indx, mode):
		'''Substitudes numbers that exceed max value witth max value.'''
		val = self.string_to_int(self.get())
		if val > self.max_val:
			self.set(str(self.max_val))
		elif val < self.min_val:
			self.set(str(self.min_val))

	#Restrict user input zeros position
	def remove_zeros(self, var, indx, mode):
		'''Removes zeros before number.'''
		val = self.get()
		if self.is_negative(val):
			if (len(val) > 1) and (val[1] == '0'):
				self.set('-'+val[2:])
		else:
			if (len(val) > 1) and (val[0] == '0'):
				self.set(val[1:])

	def limit(self, var, indx, mode):
		'''Restricts variable value.'''
		current_val = self.get()
		if len(current_val) > 0:
			changed_char_type = self.limit_char_type(var, indx, mode)
			if not changed_char_type:
				self.remove_zeros(var, indx, mode)
				self.limit_length(var, indx, mode)
				self.limit_value(var, indx, mode)