from machine import ADC,Pin,LED,Timer
import utime as time

def buzzer_toggle(t):
    if buzzer_pin.value() == 0:
        buzzer_pin.value(1)
    else :
        buzzer_pin.value(0)

buzzer_pin = Pin(Pin.epy.P22,Pin.OUT) #指定 P22 為 輸出, 推動buzzer
timer = Timer (0,freq=500) #使用 timer 0 (0-3), 產生 500Hz 中斷
timer.callback(buzzer_toggle) # 回調函數掛載 每次 500Hz 會進去回調函數

time.sleep(2) 兩秒後

timer.callback(None) # 關閉呼叫回調函數
