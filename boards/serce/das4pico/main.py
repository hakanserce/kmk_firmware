from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())
keyboard.keymap = [
    # closest to the original Das Keyboard - only Fn key is not mapped to anything, use this if you want original
    # [ 
        # KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.F13, KC.BRID, KC.BRIU,
        # KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.EJCT, KC.HOME, KC.PGUP, KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS,
        # KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS,          KC.DEL, KC.END, KC.PGDN,   KC.P7, KC.P8, KC.P9, KC.PPLS,
        # KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT,                                           KC.P4, KC.P5, KC.P6,
        # KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,                 KC.UP,                       KC.P1, KC.P2, KC.P3, KC.PENT,
        # KC.LCTL, KC.LALT, KC.LCMD, KC.SPC,                         KC.RCMD, KC.RALT, KC.NO, KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT,            KC.P0, KC.PDOT
    # ],
    # This one just adds a few multimedia keys and moust movement keys
    [ 
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12,   KC.F13, KC.BRID, KC.BRIU,
        KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC, KC.MPRV, KC.MPLY, KC.MNXT,  KC.NO, KC.NO, KC.MW_LT, KC.MW_RT,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS,          KC.VOLD, KC.MUTE, KC.VOLU, KC.NO, KC.MS_UP, KC.NO, KC.MW_UP,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT,                                           KC.MS_LT, KC.NO, KC.MS_RT,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT,                 KC.UP,                       KC.NO, KC.MS_DN, KC.P3, KC.MW_DN,
        KC.LCTL, KC.LALT, KC.LCMD, KC.SPC,                         KC.RCMD, KC.RALT, KC.NO, KC.RCTL, KC.LEFT, KC.DOWN, KC.RGHT,            KC.MB_LMB, KC.MB_RMB
    ],
]

if __name__ == '__main__':
    keyboard.go()