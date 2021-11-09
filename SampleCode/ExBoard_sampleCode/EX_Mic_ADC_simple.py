from machine import ADC,Pin,LED
import utime as time

Mic = ADC(Pin.epy.AIN2) # Lite-Ex Board Mic 使用 AIN2 Pin
# ADC 12bit => 4096 (3.3V)
# 使用 MICROPHONE 改變彩色燈條 亮度

RGB = LED(LED.RGB)

while True:
    lightness = Mic.read() / 500 * 100 # 分割ADC 讀出數值在 0-100之間 ,Mic 輸入訊號比較小 
    RGB.lightness (int ( lightness) ) # 取 lightness 整數
    for i in range(1,6):
        RGB.rgb_write(i,0,255,0)
    print(int ( lightness))
    time.sleep_ms(20)