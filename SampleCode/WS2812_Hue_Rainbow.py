'''
  micropython WS2812 RGB LED Strip rainbow
  for richlink (Taiwan) ePy Lite and RGB LED Strip demo 
  Led_number =10 -> define the WS2812 RGB LED numbers is 10
  h_step = 20 --> define the HSV Hue STEP 
  
  Author : wright@aiplaynlearn.com
  Hardware : ePy Lite + WS2812 LED Strip
'''
from machine import *
import math
import utime
i = None
RGB = LED(LED.RGB)

'''
  h = [0~360] 
  s and v =[0.0 ~ 1.0] float
  return RGB is [0~255]
'''

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b
    
Led_number =10
h_step = 20
led_a = [[0,0,0]]*Led_number

while True:
    for h in range (0,360,h_step):
        for i in range(Led_number):
            Cr,Cg,Cb = hsv2rgb(h+(i*h_step),1,1)
            led_a[i] = [Cr,Cg,Cb]
        RGB.rgb_write(led_a)
        utime.sleep_ms(100)
