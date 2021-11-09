from machine import LED
import utime as time
import _thread

#定義兩個不互相影響的 Thread(執行緒)
#閃爍 不同顏色 LED 並且帶入 閃爍時間

def LedFlash(led_obj,delay_time):

    while True :
        led_obj.toggle()
        time.sleep_ms(delay_time)
            
#規劃兩個 LED 黃色與紅色
Ledy = LED('ledy')
Ledr = LED('ledr')

#啟動執行緒 黃色 LED 每1000ms 切換依次狀態 , 帶入Ledy 物件
_thread.start_new_thread(LedFlash,(Ledy,1000,))

#啟動執行緒 紅色 LED 每500ms 切換依次狀態 帶入Ledr 物件
_thread.start_new_thread(LedFlash,(Ledr,500,))


