from machine import ADC,Pin,LED,Timer
import utime as time

def buzzer_toggle(t):
    if buzzer_pin.value() == 0:
        buzzer_pin.value(1)
    else :
        buzzer_pin.value(0)

buzzer_pin = Pin(Pin.epy.P22,Pin.OUT) #指定 P22 為 輸出, 推動buzzer

timer = Timer (0,freq=261*2) # Do
timer.callback(buzzer_toggle) # 回調函數掛載 每次 500Hz 會進去回調函數

time.sleep_ms(500) #500ms
timer = Timer (0,freq=293*2) #Re
time.sleep_ms(500) #500ms
timer = Timer (0,freq=329*2) # Mi
time.sleep_ms(500) #500ms
timer = Timer (0,freq=349*2) # Fa
time.sleep_ms(500) #500ms
timer = Timer (0,freq=391*2) # So
time.sleep_ms(500) #500ms
timer = Timer (0,freq=440*2) # La
time.sleep_ms(500) #500ms
timer = Timer (0,freq=494*2) # Si
time.sleep_ms(500) #500ms 
timer = Timer (0,freq=523*2) # Do
time.sleep_ms(500) #500ms

for tone in range(100,8000,100):
    timer = Timer (0,freq=tone) 
    time.sleep_ms(10)


timer.callback(None) # 關閉呼叫回調函數
