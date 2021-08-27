# MicroPython TM1637 quad 7-segment LED display driver examples

# WeMos D1 Mini -- 4 Digit Display
# D1 (P2) ----- CLK
# D2 (P3) ----- DIO
# 3V3 ------------ VCC
# G -------------- GND

# PCT2075 --- 溫度 Sensor +-1度
# VCC --3.3V
# GND -- GND
# SDA -- SDA0
# SCL -- SCL0


from machine import I2C,Pin,LED
import utime
import ustruct as struct
import tm1637


tm = tm1637.TM1637(clk=Pin.epy.P19, dio=Pin.epy.P18)

i2c =I2C(0,I2C.MASTER)

LED_R = LED('ledr')
LED_Y = LED('ledy')
LED_Y.off()

PCT2075_ADDR = 72
#PCT2075_ADDR = 55
temp = bytearray(2)
counter = 0
try :

    while True:
        if i2c.is_ready(PCT2075_ADDR) :
          
            temp=i2c.recv(2,PCT2075_ADDR)
            T = struct.unpack('>h',temp) 
            temp_c = int (T[0])/32*125/1000 
            temp_c = round(temp_c,2)  
            print ('{}.{}'.format(int(temp_c),int (temp_c*0.1*100)))
            tm.show('{}{}'.format(int(temp_c),int (temp_c*0.1*100)),True) 
            LED_Y.on()
            utime.sleep_ms(300)
        else:
            LED_Y.off()
            LED_R.on()
            utime.sleep_ms(300)
            LED_R.off()
            utime.sleep_ms(300)
            i2c.deinit()                 
            tm.show('No')   
            i2c =I2C(0,I2C.MASTER)
except :
    tm.show(' Err')  
    