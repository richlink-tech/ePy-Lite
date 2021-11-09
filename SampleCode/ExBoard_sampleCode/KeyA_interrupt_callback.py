from machine import LED,Switch #引用 內建(Switch) 按鍵功能物件
import utime as time

RGB = LED(LED.RGB) #使用Lite 特有WS2812B(RGB LED) 驅動
keya = Switch('keya')

times =  0 #定義一變數

def _按鍵壓下執行():
    global times #使用全區域變數
    times += 1  # times = times+1

keya.callback(_按鍵壓下執行) #指定按下按鍵中斷執行程序

while True: 
    RGB.lightness(times)
    for i in range (1,times):
        RGB.rgb_write( i , 255 ,0 ,0) 


    
