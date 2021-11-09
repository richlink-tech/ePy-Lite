from machine import LED
import utime as time

RGB = LED(LED.RGB) #使用Lite 特有WS2812B(RGB LED) 驅動 

#單顆控制 RGB = 0 LED 不亮
RGB.rgb_write( 1 , 255 ,0 ,0) # 指定第1個 RGB燈 , R=255 /G=0 /B=0
RGB.rgb_write( 2 , 0 ,255 ,0) # 指定第2個 RGB燈 , R=0 /G=255 /B=0
RGB.rgb_write( 3 , 0 ,0 ,255) # 指定第3個 RGB燈 , R=0 /G=0 /B=255

time.sleep(1)
#多顆 RGB LED 一起控制 (使用List )

Color = [ [0,100,0] , [255,100 ,0] , [100 ,10 ,100] ] #指定前三個 RGB LED RGB顏色
RGB.rgb_write( Color)
time.sleep(1)

#rgb write前可控制亮度 1-100
RGB.lightness(100)
RGB.rgb_write( Color)

#使用迴圈製作 RGB LED 漸漸變亮
for lightness in range(1,100,10): 
    RGB.lightness(lightness)
    RGB.rgb_write( Color)
    time.sleep_ms(500)
