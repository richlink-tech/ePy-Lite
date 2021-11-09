from machine import LED
import utime as time
import _thread
import math

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h = h*360
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

#定義兩個不互相影響的 Thread(執行緒)
#閃爍 不同顏色 LED 並且帶入 閃爍時間

def LedFlash(led_obj,delay_time,color,led_num):
    times = 0
    while True :
        if lock.acquire():
            if times == 0 :
                led_obj.rgb_write(led_num,color[0],color[1],color[2])
                times = 1
            else:
                led_obj.rgb_write(led_num,0,0,0)
                times = 0
            lock.release()
        time.sleep_ms(delay_time)
            
#規劃兩個 LED 黃色與紅色
Led = LED(LED.RGB)
lock = _thread.allocate_lock()

for index in range(1,6):
    srgb = hsv2rgb (1/5*index,1,1)
    _thread.start_new_thread(LedFlash,(Led,500+200*index,(srgb[0],srgb[1],srgb[2]),index,))


