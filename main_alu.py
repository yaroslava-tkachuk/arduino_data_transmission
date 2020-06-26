import serial

from alu_simulator import ALUsimulator


if __name__ == '__main__':
    try:
        alu = ALUsimulator()
        alu.configure_window()
        alu.place_elements()
        alu.mainloop()
    except serial.serialutil.SerialException:
        print('Please, connect your Arduino to PC and try again.')