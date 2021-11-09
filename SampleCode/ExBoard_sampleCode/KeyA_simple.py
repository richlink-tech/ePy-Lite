from machine import LED,Switch #引用 內建 按鍵功能物件
import utime as time

RGB = LED(LED.RGB) #使用Lite 特有WS2812B(RGB LED) 驅動
keya = Switch('keya')

while True: #使用無限迴圈 持續讀取按鍵

    if keya.value() == True : # value() = True 表示按鍵按下
        RGB.off()  #清除所有 RGB LED
        RGB.rgb_write( 1 , 255 ,0 ,0) # 指定第1個 RGB燈 , R=255 /G=0 /B=0
    else:    # value() = False 表示按鍵放開
        RGB.off() #清除所有 RGB LED
        RGB.rgb_write( 2 , 255 ,0 ,0) # 指定第2個 RGB燈 , R=255 /G=0 /B=0

    
