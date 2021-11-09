from machine import LED
import utime as time

ledy = LED('ledy') #Lite 板上的三種顏色 LED
ledr = LED('ledr')
ledg = LED('ledg')

ledy.on() #開啟
time.sleep_ms(500) # delay 500ms
ledy.off() #關閉

ledr.on()
time.sleep(1) #delay 1 sec
ledr.toggle() #切換開或關

ledg.off ()
time.sleep_us(1000000) #delay 1000000us = 1000ms = 1sec
ledg.on ()
