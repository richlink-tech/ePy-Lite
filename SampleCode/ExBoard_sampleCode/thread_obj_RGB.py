from machine import LED
import utime as time
import _thread

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

#啟動執行緒 黃色 LED 每1000ms 切換依次狀態 , 帶入Ledy 物件
_thread.start_new_thread(LedFlash,(Led,1000,(255,0,0),1,))

#啟動執行緒 紅色 LED 每500ms 切換依次狀態 帶入Ledr 物件
_thread.start_new_thread(LedFlash,(Led,500,(0,255,0),2,))


