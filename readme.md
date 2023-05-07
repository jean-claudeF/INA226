# INA226 Micropython library 
This lib is partly based on the one that Chris Becker designed:
https://github.com/elschopi/TI_INA226_micropython

There are 2 ways to use it.
The easiest one is like this:

```py
import ina226_jcf as ina226      
from machine import Pin, I2C
import time

i2c = I2C(0,scl=Pin(9), sda=Pin(8), freq=100000)
ina = ina226.INA226(i2c, 0x40, Rs = 0.002, voltfactor = 2 )       # Rs = 2mOhm, bus voltage divider by 2 for 0...72V range
                                                                  # In this case Rs must be low side!
i=0
while True:
       
    # Get voltage, current and power by using only Bus and Shunt voltage registers
    # This is easier, should be with best accuracy and no register overflow problems:
    v, i, p = ina.get_VIP()
    V = '%2.3f' % v
    I = '%2.3f' % i
    P = '%2.3f' % p
    print(i, '\t', V, '\t', I, '\t',  P)
``` 
The example above uses only the Bus voltage register and the Shunt voltage register, so no calibration has to be done.

You may also use the Calibration, Current and Power registers. In this case you have to set the calibration:
```py
import ina226_jcf as ina226      

from machine import Pin, I2C
import time


i2c = I2C(0,scl=Pin(9), sda=Pin(8), freq=100000)
ina = ina226.INA226(i2c, 0x40, Rs = 0.002, voltfactor = 2 )       # Rs = 2mOhm, bus voltage divider by 2 for 0...72V range
                                                                  # In this case Rs must be low side!

ina.set_calibration_custom( calValue=2560)                        
ina.set_current_lsb  (0.001)

i=0
while True:
     
    # Get voltage, current and power using Calibration, Current and Power registers,
    # as TI wants us to do. Is probably faster, but calibration register must be set:
    v, i, p = ina.get_VIP_TI()
    V = '%2.3f' % v
    I = '%2.3f' % i
    P = '%2.3f' % p
    print(i, '\t',V, '\t', I, '\t',  P)
```

TO DO:
Add a comfortable function to set configuration options like averaging etc.

