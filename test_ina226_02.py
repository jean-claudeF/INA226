''' Simple ina226 program to read voltage, current and power'''




import ina226_jcf as ina226      # corrected bug 2.5uV instaed of 10uV for UsLSB, added register read functions
# https://github.com/elschopi/TI_INA226_micropython
#  Christian Becker and JCF

from machine import Pin, I2C
import time


i2c = I2C(0,scl=Pin(9), sda=Pin(8))
ina = ina226.INA226(i2c, 0x40)

#ina.set_calibration(calValue )                   # default configuration and calibration value
#ina.set_calibration_custom( calValue=25600)       # gives correct values with chris's lib though not the calculated value!
ina.set_calibration_custom( calValue=5120)      

def get_vip(kv = 2):
    v = kv * ina.bus_voltage
    i = ina.current
    p = kv * ina.power
    return v, i, p

#------------------------------------------
# DEBUGGING:
while True:
    vr = ina.busvoltage_register
    sr = ina.shunt_register
    ir = ina.current_register
    pr = ina.power_register
    
    v, i, p = get_vip(kv = 2)
    V = '%2.3f' % v
    I = '%2.3f' % i
    P = '%2.3f' % p
    
    print(vr, '\t', sr, '\t', ir,'\t', pr,'\t', V, '\t', I, '\t', P,'\t', ina.shunt_voltage)
    time.sleep(2)
    
#-----------------------------------
'''
secs = 0
while True:
        
    if (secs % 10 == 0):
        print("#t/s", '\t', "u/V", '\t', "i/A", '\t', "p/W")
    
    v, i, p = get_vip(kv = 2)
    V = '%2.3f' % v
    I = '%2.3f' % i
    P = '%2.3f' % p
    print(secs, '\t', V, '\t', I, '\t', P, ina.shunt_voltage)
    
    time.sleep(1)
    secs += 1
'''