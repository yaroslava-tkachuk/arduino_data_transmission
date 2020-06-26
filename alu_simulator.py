from tkinter import Tk, PhotoImage, Label, Frame, Entry, StringVar, Button

from limited_string_var import LimitedStringVar
from serial_bus import SerialBus


class ALUsimulator(Tk):

	'''Simuates 8-bit ALU operations.'''

	def __init__(self):
		super().__init__()
		#Window configuration attributes
		self._title_str = 'ALU SIMULATOR'
		self._bg_image = PhotoImage(file='./alu_background.png')
		self._bg_label = Label(self, image=self.bg_image)
		self._frame_color = '#C8CACC'
		self._label_text_color = '#000000'
		self._frame = Frame(self, width=285, height=230, bg=self.frame_color)
		#Window elements
		#Labels
		self._input_a_label = Label(self.frame, text='INPUT A', width=7,
								   bg=self.frame_color, 
								   fg=self.label_text_color)
		self._input_b_label = Label(self.frame, text='INPUT B', width=7,
								   bg=self.frame_color,
								   fg=self.label_text_color)
		self._output_label = Label(self.frame, text='OUTPUT', width=7,
								  bg=self.frame_color,
								  fg=self.label_text_color)
		self._carry_label = Label(self.frame, text='CARRY', width=7,
								 bg=self.frame_color,
								 fg=self.label_text_color)
		self._status_label = Label(self.frame, text='OPERATION STATUS',
								  width=15, bg=self.frame_color,
								  fg=self.label_text_color)
		#Inputs
		self._a_var = LimitedStringVar()
		self._b_var = LimitedStringVar()
		self._input_a = Entry(self.frame, borderwidth=3, width=7,
							 textvariable=self.a_var)
		self._input_b = Entry(self.frame, borderwidth=3, width=7,
							 textvariable=self.b_var)
		#Outputs
		self._output_var = StringVar()
		self._carry_var = StringVar()
		self._status_var = StringVar()
		self._output = Label(self.frame, textvariable=self.output_var,
							width=7)
		self._carry = Label(self.frame, textvariable=self.carry_var, width=7)
		self._status = Label(self.frame, textvariable=self.status_var, 
							width=39)
		#Buttons
		self._add_button = Button(self.frame, text='ADD', width=6, height=3,
								 command = lambda opcode=0:\
								 self.button_click(opcode))
		self._sub_button = Button(self.frame, text='SUB', width=6, height=3,
								 command = lambda opcode=1:\
								 self.button_click(opcode))
		self._and_button = Button(self.frame, text='AND', width=6, height=3,
								 command = lambda opcode=2:\
								 self.button_click(opcode))
		self._or_button = Button(self.frame, text='OR', width=6, height=3,
								command = lambda opcode=3:\
								self.button_click(opcode))
		self._xor_button = Button(self.frame, text='XOR', width=6, height=3,
								 command = lambda opcode=4:\
								 self.button_click(opcode))
		self._not_button = Button(self.frame, text='NOT', width=6, height=3,
								 command = lambda opcode=5:\
								 self.button_click(opcode))
		self._shift_right_button = Button(self.frame, text='>>', width=6,
										 height=3, command = lambda opcode=6:\
										 self.button_click(opcode))
		self._shift_left_button = Button(self.frame, text='<<', width=6,
									    height=3, command = lambda opcode=7:\
									    self.button_click(opcode))
		#Communication module
		self._serial_bus = SerialBus()

	#Getters
	@property
	def title_str(self):
		return self._title_str

	@property
	def bg_image(self):
		return self._bg_image

	@property
	def bg_label(self):
		return self._bg_label

	@property
	def frame_color(self):
		return self._frame_color

	@property
	def label_text_color(self):
		return self._label_text_color

	@property
	def frame(self):
		return self._frame

	@property
	def input_a_label(self):
		return self._input_a_label

	@property
	def input_b_label(self):
		return self._input_b_label

	@property
	def output_label(self):
		return self._output_label

	@property
	def carry_label(self):
		return self._carry_label

	@property
	def status_label(self):
		return self._status_label

	@property
	def a_var(self):
		return self._a_var

	@property
	def b_var(self):
		return self._b_var

	@property
	def input_a(self):
		return self._input_a

	@property
	def input_b(self):
		return self._input_b
	
	@property
	def output_var(self):
		return self._output_var

	@property
	def carry_var(self):
		return self._carry_var

	@property
	def status_var(self):
		return self._status_var

	@property
	def output(self):
		return self._output

	@property
	def carry(self):
		return self._carry

	@property
	def status(self):
		return self._status

	@property
	def add_button(self):
		return self._add_button

	@property
	def sub_button(self):
		return self._sub_button

	@property
	def and_button(self):
		return self._and_button

	@property
	def or_button(self):
		return self._or_button

	@property
	def xor_button(self):
		return self._xor_button

	@property
	def not_button(self):
		return self._not_button

	@property
	def shift_left_button(self):
		return self._shift_left_button

	@property
	def shift_right_button(self):
		return self._shift_right_button

	@property
	def serial_bus(self):
		return self._serial_bus
	
	#Setters
	@title_str.setter
	def title_str(self, new_title_str):
		self._title_str = new_title_str

	@bg_image.setter
	def bg_image(self, new_bg_image):
		self._bg_image = new_bg_image

	@bg_label.setter
	def bg_label(self, new_bg_label):
		self._bg_label = new_bg_label

	@frame_color.setter
	def frame_color(self, new_frame_color):
		self._frame_color = new_frame_color

	@label_text_color.setter
	def label_text_color(self, new_label_text_color):
		self._label_text_color = new_label_text_color

	@frame.setter
	def frame(self, new_frame):
		self._frame = new_frame

	@input_a_label.setter
	def input_a_label(self, new_input_a_label):
		self._input_a_label = new_input_a_label

	@input_b_label.setter
	def input_b_label(self, new_input_b_label):
		self._input_b_label = new_input_b_label

	@output_label.setter
	def output_label(self, new_output_label):
		self._output_label = new_output_label

	@carry_label.setter
	def carry_label(self, new_carry_label):
		self._carry_label = new_carry_label

	@status_label.setter
	def status_label(self, new_status_label):
		self._status_label = new_status_label

	@a_var.setter
	def a_var(self, new_a_var):
		self._a_var = new_a_var

	@b_var.setter
	def b_var(self, new_b_var):
		self._b_var = new_b_var

	@input_a.setter
	def input_a(self, new_input_a):
		self._input_a = new_input_a

	@input_b.setter
	def input_b(self, new_input_b):
		self._input_b = new_input_b
	
	@output_var.setter
	def output_var(self, new_output_var):
		self._output_var = new_output_var

	@carry_var.setter
	def carry_var(self, new_carry_var):
		self._carry_var = new_carry_var

	@status_var.setter
	def status_var(self, new_status_var):
		self._status_var = new_status_var

	@output.setter
	def output(self, new_output):
		self._output = new_output

	@carry.setter
	def carry(self, new_carry):
		self._carry = new_carry

	@status.setter
	def status(self, new_status):
		self._status = new_status

	@add_button.setter
	def add_button(self, new_add_button):
		self._add_button = new_add_button

	@sub_button.setter
	def sub_button(self, new_sub_button):
		self._sub_button = new_sub_button

	@and_button.setter
	def and_button(self, new_and_button):
		self._and_button = new_and_button

	@or_button.setter
	def or_button(self, new_or_button):
		self._or_button = new_or_button

	@xor_button.setter
	def xor_button(self, new_xor_button):
		self._xor_button = new_xor_button

	@not_button.setter
	def not_button(self, new_not_button):
		self._not_button = new_not_button

	@shift_left_button.setter
	def shift_left_button(self, new_shift_left_button):
		self._shift_left_button = new_shift_left_button

	@shift_right_button.setter
	def shift_right_button(self, new_shift_right_button):
		self._shift_right_button = new_shift_right_button

	@serial_bus.setter
	def serial_bus(self, new_serial_bus):
		self._serial_bus = new_serial_bus

	def configure_window(self):
		'''Configures the window.'''
		self.resizable(False, False)
		self.title(self.title_str)
		self.geometry(str(self.bg_image.width())+'x'+\
					 str(self.bg_image.height()))
		self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
		self.frame.place(x=141, y=123)

	def place_elements(self):
		'''Places window elements.'''
		#Labels
		self.input_a_label.grid(row=0, column=0,
							   padx=(7.625, 12.5), pady=(7.625, 0))
		self.input_b_label.grid(row=0, column=1,
							   padx=(7.625, 12.5), pady=(7.625, 0))
		self.output_label.grid(row=0, column=2,
							  padx=(7.625, 12.5), pady=(7.625, 0))
		self.carry_label.grid(row=0, column=3,
							 padx=(7.625, 12.5), pady=(7.625, 0))
		self.status_label.grid(row=4, column=1, columnspan=2,
							  padx=(7.625, 12.5))
		#Inputs
		self.input_a.grid(row=1, column=0)
		self.input_b.grid(row=1, column=1)
		#Outputs
		self.output.grid(row=1, column=2)
		self.carry.grid(row=1, column=3)
		self.status.grid(row=5, column=0, columnspan=4, pady=(0, 2))
		#Buttons
		self.add_button.grid(row=2, column=0, pady=(15, 5))
		self.sub_button.grid(row=3, column=0, pady=(5, 0))
		self.and_button.grid(row=2, column=1, pady=(15, 5))
		self.or_button.grid(row=3, column=1, pady=(5, 0))
		self.xor_button.grid(row=2, column=2, pady=(15, 5))
		self.not_button.grid(row=3, column=2, pady=(5, 0))
		self.shift_right_button.grid(row=2, column=3, pady=(15, 5))
		self.shift_left_button.grid(row=3, column=3, pady=(5, 0))
		
	def update_output(self, new_output):
		'''Updates output.'''
		self.output_var.set(new_output)

	def update_carry(self, new_carry):
		'''Updates carry.'''
		self.carry_var.set(new_carry)

	def update_status(self, new_status):
		'''Updates operation status field.'''
		self.status_var.set(new_status)

	def show_result(self, result, carry):
		'''Updates operation result and status fields.'''
		self.update_output(str(result))
		self.update_carry(str(carry))
		self.update_status('SUCCESS. Operation has been completed.')

	def click_react(self, opcode, a, b):
		'''Processes data, formats result, updates output and carry.'''
		error_message = 'FAIL. Transmission problem. Please, try again.'
		output = self.serial_bus.perform_operation(opcode, a, b)
		if output is not None:
			result, carry = self.serial_bus.format_output(output)
			self.show_result(result, carry)
		else:
			self.update_status(error_message)

	def two_op_react(self, opcode, a, b):
		'''Verifies input and reacts to 2-operand button click.'''
		if ((a != '') and (b != '')):
			self.click_react(opcode, int(a), int(b))
		else:
			self.update_status('Please provide A and B operands.')

	def one_op_react(self, opcode, a):
		'''Verifies input and reacts to 1-operand button click.'''
		if (a != ''):
			self.click_react(opcode, int(a), None)
		else:
			self.update_status('Please provide A operand.')

	def button_click(self, opcode=None):
		'''Reacts on a button click.'''
		a = self.a_var.get()
		b = self.b_var.get()
		if opcode < 5:
			self.two_op_react(opcode, a, b)
		else:
			self.one_op_react(opcode, a)