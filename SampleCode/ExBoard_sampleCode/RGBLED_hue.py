from machine import ADC,Pin,LED
import utime as time
import math

def hsv2rgb(h, s, v):
    h = float(h) * 360
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
    r, g, b = [(v, t, p),(q, v, p),(p, v, t),(p, q, v),(t, p, v),(v, p, q)][hi]
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return r, g, b

def proc_RGBLED (Strip_data,num_led,hue_start,hue_step):

    for index in range (num_led):
        srgb = hsv2rgb(hue_start+hue_step*index , 1 , 1)
        Strip_data[index] =[srgb[0],srgb[1],srgb[2]]
        


RGB = LED(LED.RGB)
RGB.lightness(100)

