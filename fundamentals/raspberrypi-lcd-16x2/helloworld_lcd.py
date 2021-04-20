import drivers
from time import *

lcd = drivers.lcd()
lcd.lcd_display_string("Hello World!", 1)
