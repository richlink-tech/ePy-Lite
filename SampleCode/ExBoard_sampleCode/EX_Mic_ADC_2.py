from machine import ADC,Pin,LED
import utime as time


Mic = ADC(Pin.epy.AIN2) # Lite-Ex Board Mic 使用 AIN2 Pin
# ADC 12bit => 4096 (3.3V)
# 使用 MICROPHONE 改變彩色燈條 亮度

RGB = LED(LED.RGB)
Vol_list = [0]*10
rrr = [[0,255,0]]*5
while True:
    Vol_list.pop(0) # 刪除最前一筆Mic 錄音資料
    lightness = Mic.read() / 500 * 100 # 分割ADC 讀出數值在 0-100之間 ,Mic 輸入訊號比較小
    Vol_list.append(lightness) # 增加最新一筆資料在最後
    move_avg = int (sum(Vol_list)/10) # 計算10個Mic 錄音的音量移動平均值, 
    RGB.lightness (move_avg *5)  # 依據移動平均改變 RGB LED 亮度
    RGB.rgb_write(rrr)

