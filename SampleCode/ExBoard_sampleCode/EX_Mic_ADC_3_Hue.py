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
        
Mic = ADC(Pin.epy.AIN2) # Lite-Ex Board Mic 使用 AIN2 Pin
# ADC 12bit => 4096 (3.3V)
# 使用 MICROPHONE 改變彩色燈條 亮度

RGB = LED(LED.RGB)
Vol_list = [0]*10
Strip = [[0,255,0]]*5
Vol_level = [5,10,20,40,40]

proc_RGBLED (Strip,5 ,0.2, -0.4/5)

RGB.lightness(100)

while True:
    Vol_list.pop(0) # 刪除最前一筆Mic 錄音資料
    vol = Mic.read() / 200 *100 # 分割ADC 讀出數值在 0-100之間 ,Mic 輸入訊號比較小
    #print(vol)
    Vol_list.append(vol) # 增加最新一筆資料在最後

    move_avg = int (sum(Vol_list)/10) # 計算10個Mic 錄音的音量移動平均值, 
    RGB.off()

    if move_avg == 0:
        RGB.off()
    else:    
        if move_avg <= Vol_level [0]:
            Show_Strip = Strip [:1]
        elif move_avg <= Vol_level [1]:
            Show_Strip = Strip [:2]
        elif move_avg <= Vol_level [2]:
            Show_Strip = Strip [:3]
        elif move_avg <= Vol_level [3]:
            Show_Strip = Strip [:4]
        else :
            Show_Strip = Strip
            
        RGB.rgb_write(Show_Strip)
