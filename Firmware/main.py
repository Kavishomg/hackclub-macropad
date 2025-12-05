print("Starting Macropad Firmware...")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData
from kmk.extensions.RGB import RGB

# Initialize the Keyboard
keyboard = KMKKeyboard()

# -------------------------------------------------------------------------
# 1. PINS & MATRIX SETUP (Matches the Schematic)
# -------------------------------------------------------------------------
# Switches SW1-SW5 are on Pins: 26, 27, 28, 29, 3
keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29, board.GP3)
# We assume direct wiring (no matrix grid), so no row pins needed
keyboard.row_pins = (board.GP26, board.GP27, board.GP28, board.GP29, board.GP3) 

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# -------------------------------------------------------------------------
# 2. ROTARY ENCODER SETUP
# -------------------------------------------------------------------------
# Encoder A/B on GP0 and GP1. Button on GP2.
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP0, board.GP1, board.GP2, False),)
keyboard.modules.append(encoder_handler)

# -------------------------------------------------------------------------
# 3. OLED DISPLAY SETUP
# -------------------------------------------------------------------------
# I2C on GP6 (SDA) and GP7 (SCL)
oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC, 1:["Layer"]},
        corner_two={0:OledReactionType.LAYER, 1:["1", "2", "3", "4"]},
        corner_three={0:OledReactionType.STATIC, 1:["HackClub"]},
        corner_four={0:OledReactionType.STATIC, 1:["Macropad"]}
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)
keyboard.extensions.append(oled_ext)

# -------------------------------------------------------------------------
# 4. RGB LED SETUP (Underglow)
# -------------------------------------------------------------------------
# Data Pin on GP4
rgb = RGB(pixel_pin=board.GP4, num_pixels=2, val_limit=100, hue_default=0, sat_default=255, val_default=100)
keyboard.extensions.append(rgb)

# -------------------------------------------------------------------------
# 5. KEYMAP
# -------------------------------------------------------------------------
# Add Media Keys support
keyboard.extensions.append(MediaKeys())

# SW1, SW2, SW3, SW4, SW5, Encoder_Button
keyboard.keymap = [
    [
        # Layer 0: Media Control
        KC.MPLY,    # SW1: Play/Pause
        KC.MNXT,    # SW2: Next Track
        KC.MPRV,    # SW3: Prev Track
        KC.COPY,    # SW4: Copy
        KC.PASTE,   # SW5: Paste
        KC.MUTE,    # Encoder Click: Mute
    ]
]

# Encoder Rotation Map (Volume Up / Volume Down)
encoder_handler.map = [ ((KC.VOLD, KC.VOLU, KC.MUTE),) ]

if __name__ == '__main__':
    keyboard.go()
