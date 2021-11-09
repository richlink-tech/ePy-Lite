from machine import ADC,Pin,LED
import utime as time

VR = ADC(Pin.epy.AIN5) # Lite-Ex Board 可變電阻使用 AIN5 Pin
# ADC 12bit => 4096 (3.3V)
# 使用 VR 改變彩色燈條 亮度

RGB = LED(LED.RGB)

while True:
    lightness = VR.read() / 4096 * 100 # 分割VR 讀出數值在 0-100之間
    RGB.lightness (int ( lightness) ) # 取 lightness 整數
    for i in range(1,6):
        RGB.rgb_write(i,0,255,0)
    time.sleep_ms(500)