import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

rows = [1, 2, 5, 7, 16, 21, 22, 26]
cols = [0, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 28]
def coord(row, col):
    return rows.index(row)*len(cols) + cols.index(col)


class KMKKeyboard(_KMKKeyboard):
    
    # TODO: remove duplication here. Generate row_pins and col_pins, from rows/cols
    row_pins = [
        board.GP1,
        board.GP2,
        board.GP5, 
        board.GP7, 
        board.GP16,
        board.GP21,
        board.GP22,
        board.GP26
    ]
    col_pins = [
        board.GP0, 
        board.GP3, 
        board.GP4, 
        board.GP6,
        board.GP8, 
        board.GP9, 
        board.GP10, 
        board.GP11, 
        board.GP12, 
        board.GP13, 
        board.GP14, 
        board.GP15, 
        board.GP17, 
        board.GP18, 
        board.GP19,
        board.GP20,
        board.GP28
        ]
    diode_orientation = DiodeOrientation.ROW2COL

    coord_mapping = [
        coord(21,28), coord(5,8), coord(5,9), coord(7,9), coord(21,9), coord(1,3), coord(21,12), coord(7,6), coord(5,6), coord(5,4), coord(1,4), coord(21,4), coord(22,4), coord(1,0), coord(2,0), coord(2,3), 
        coord(5,28), coord(1,28), coord(1,8), coord(1,9), coord(1,10), coord(5,10), coord(5,11), coord(1,11), coord(1,12), coord(1,6), coord(1,13), coord(5,13), coord(5,12), coord(7,4), coord(5,15), coord(5,20), coord(5,19), coord(16,14), coord(16,15), coord(16,19), coord(22,19), 
        coord(7,28), coord(2,28), coord(2,8), coord(2,9), coord(2,10), coord(7,10), coord(7,11), coord(2,11), coord(2,12), coord(2,6), coord(2,13), coord(7,13), coord(7,12), coord(26,4), coord(5,14), coord(1,20), coord(1,19), coord(2,14), coord(2,15), coord(2,19), coord(2,20), 
        coord(7,8), coord(26,28), coord(26,8), coord(26,9), coord(26,10), coord(21,10), coord(21,11), coord(26,11), coord(26,12), coord(26,6), coord(26,13), coord(21,13), coord(16,4), coord(7,14), coord(7,15), coord(7,19), 
        coord(7,18), coord(16,28), coord(16,8), coord(16,9), coord(16,10), coord(22,10), coord(22,11), coord(16,11), coord(16,12), coord(16,6), coord(22,13), coord(26,18), coord(21,20), coord(26,14), coord(26,15), coord(26,19), coord(26,20), 
        coord(5,3), coord(7,17), coord(21,0), coord(21,14), coord(22,0), coord(26,17), coord(22,6), coord(16,3), coord(22,20), coord(22,14), coord(22,15), coord(21,15), coord(21,19)
    ]
