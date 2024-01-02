import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    row_pins = [board.GP2, board.GP7, board.GP26]
    col_pins = [board.GP14, board.GP15, board.GP19]
    diode_orientation = DiodeOrientation.ROW2COL

    coord_mapping = [
        0, 1, 2,
        3, 4, 5,
        6, 7, 8, 
    ]




    extensions = []