import board
import digitalio
import time


# This is a class that helps finding which pins are connected to which key as row,col
# in a keyboard matrix.
# Especially useful if you are working with an old keyboard, or replacing the controller
# of a commercial keyboard.
#
# Example usage: in code.py put the following 3 lines of code
#
# from tools.pico_matrix_helper import PicoMatrixHelper
# 
# helper = PicoMatrixHelper()
# helper.start()

class PicoMatrixHelper:
    def start(self):
        # Get all available GPIO pins on the Raspberry Pi Pico
        non_gpio_pins = [23, 24, 25]
        all_pin_names = [f"GP{p}" for p in range(0, 29) if p not in non_gpio_pins]
        all_pins = {p : digitalio.DigitalInOut(getattr(board,p)) for p in all_pin_names}

        try:
            #first set all to input mode
            for pin_name in all_pin_names:
                pin = all_pins[pin_name]
                pin.switch_to_input(pull=digitalio.Pull.DOWN)

            while True:
                for pin1_name in all_pin_names:
                    pin1 = all_pins[pin1_name]
                    pin1.switch_to_output()
                    pin1.value = True
                    time.sleep(0.01)
                    for pin2_name in all_pin_names:
                        pin2 = all_pins[pin2_name]
                        if pin1 != pin2:
                            connected = pin2.value
                            if connected:
                                print(f"({pin1_name},{pin2_name})")
                            #print(f"{pin1} can write and {pin2} can read: {connected}")
                    pin1.value = False
                    pin1.switch_to_input(pull=digitalio.Pull.DOWN)
                    time.sleep(0.01)

        except KeyboardInterrupt:
            pass