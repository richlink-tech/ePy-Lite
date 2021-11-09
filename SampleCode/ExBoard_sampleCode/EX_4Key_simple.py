from machine import Pin,LED
import utime as time

UpKey = Pin(Pin.epy.P24,Pin.IN)
DownKey = Pin(Pin.epy.P8,Pin.IN)
LeftKey = Pin(Pin.epy.P6,Pin.IN)
RightKey = Pin(Pin.epy.P7,Pin.IN)

RGB = LED(LED.RGB)

# Key按下  IO讀取到為 "0"
# 依據按下按鍵 決定顯示哪一個RGB LED
while True:
    if UpKey.value() == 0:
        RGB.rgb_write(1,255,0,0)
    elif  DownKey.value()== 0:
        RGB.rgb_write(2,255,0,0)
    elif  RightKey.value() == 0:
        RGB.rgb_write(3,255,0,0)
    elif  LeftKey.value() == 0:
        RGB.rgb_write(4,255,0,0)
    time.sleep_ms(500)
    RGB.off()