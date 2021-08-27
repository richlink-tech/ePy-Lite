from machine import LED
from machine import Timer,Pin
from machine import RTC,Switch

'''
s1~s4 for Digit select --> P0~P4
seg[0]~[7] is 7Seg ABCDEFG ---> P6~P13
'''

seg =[None]*8
digits = [0b11111101,0b01100001,0b11011011, 0b11110011,0b01100111,0b10110111,0b10111111,0b11100001,0b11111111,0b11100111]

def WriteDigit(d):
    bits = [digits[d] >> i & 1 for i in range(7,-1,-1)]
    for p in range(0,7):
            seg[p].value(bits[p])
  
def tick(timer):
    global scan_line
    scan_line += 1
    if (scan_line > 3):
        scan_line = 0;
      
  
tim = Timer(3,freq = 200)
tim.callback (tick)

s1 = Pin(Pin.epy.P0,Pin.OUT)
s2 = Pin(Pin.epy.P1,Pin.OUT)
s3 = Pin(Pin.epy.P4,Pin.OUT)
s4 = Pin(Pin.epy.P5,Pin.OUT)

s1.value(1)
s2.value(1)
s3.value(1)
s4.value(1)

seg[0] = Pin(Pin.epy.P6,Pin.OUT)
seg[1] = Pin(Pin.epy.P7,Pin.OUT)
seg[2] = Pin(Pin.epy.P8,Pin.OUT)
seg[3] = Pin(Pin.epy.P9,Pin.OUT)
seg[4] = Pin(Pin.epy.P10,Pin.OUT)
seg[5] = Pin(Pin.epy.P11,Pin.OUT)
seg[6] = Pin(Pin.epy.P12,Pin.OUT)
seg[7] = Pin(Pin.epy.P13,Pin.OUT)


scan_line = 0
dot_time = 0
rtc = RTC()
rtc.datetime((2021,4,1,1,00,35,18,0))

while True:
    time = rtc.datetime()
    
    if scan_line == 0 :
        s4.value(1)
        
        WriteDigit(time[5]%10)
              
        s1.value(0)

    if scan_line == 1 :
        dot_time+=1
        s1.value(1)
        if dot_time < 400:
            seg[7].value(0)
        elif dot_time > 400 and dot_time < 800 :
            seg[7].value(1) 
        elif dot_time >800:
            dot_time = 0
                
        WriteDigit(time[5]//10)
        s2.value(0)
 
    if scan_line == 2 :

        s2.value(1)
        WriteDigit(time[4]%10)
        s3.value(0)

    if scan_line == 3 :

        s3.value(1)
        WriteDigit(time[4]//10)
        s4.value(0) 

   