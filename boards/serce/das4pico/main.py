from kb import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.I, KC.J],
    [KC.N1, KC.N2, KC.N3, KC.D, KC.E, KC.F, KC.G, KC.I, KC.J],
]

if __name__ == '__main__':
    keyboard.go()