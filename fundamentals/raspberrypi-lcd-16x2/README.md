# Raspberry Pi LCD 16x2 I²C python driver



## Required Hardware Parts

* Display with a HD44780 controller
* I2C Display Adapter
* Jumper Cable

## Installation

If you have already connected the display, you can now test whether it has been detected (if you have one of the first Raspberry Pi’s, you have to pass 0 instead of 1):

```
sudo i2cdetect -y 1
```

     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- 27 -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --


Before we can start, two I²C tools are needed, which we install:

```
sudo apt-get install python-smbus i2c-tools
```

Then we will release I2C (if you have already released it from previous tutorials, you can skip it):

```
sudo raspi-config
```

Under “Interfacing Options”> “I2C” we activate it. Now add the corresponding entries to the modules file:

Check the content of the modules file and add missing line as below

```
sudo nano /etc/modules
```

i2c-bcm2708
i2c-dev
snd-bcm2835

![alt text](https://github.com/[username]/[reponame]/blob/[branch]/etc_mod.png)


Afterwards it has to be restarted, so that all changes take effect.

```
sudo reboot
```

## PROGRAMMING THE LCD

We’ll be using Python to program the LCD, so if this is your first time writing/running a Python program, 
you may want to check out How to Write and Run a Python Program on the Raspberry Pi before proceeding.

## INSTALLING THE LIBRARY

The drivers directory content the relevant I2C library (i2c_lcd_driver.py) needed to interact with the lcd. 

## Usage 

The following is a bare minimum “Hello World!” program to demonstrate how to initialize the LCD:

```python
import drivers
from time import *

lcd = drivers.lcd()
lcd.lcd_display_string("Hello World!", 1)
```


To run it just run the python script with folllowing command:


```
python3 helloworld_lcd.py
```

## Contributing



## License



## Contact

