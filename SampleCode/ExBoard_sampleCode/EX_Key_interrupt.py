from machine import Pin,LED,Timer
import utime as time

UpKey = Pin(Pin.epy.P24,Pin.IN)
DownKey = Pin(Pin.epy.P8,Pin.IN)
LeftKey = Pin(Pin.epy.P6,Pin.IN)
RightKey = Pin(Pin.epy.P7,Pin.IN)

Key_Table = [UpKey,DownKey,LeftKey,RightKey]

def IO_callback(pin):
    ledy.toggle()
    pass

ledy = LED('ledy')
#IRQ_RISING,Pin.IRQ_FALLING , IRQ_HIGH , IRQ_LOW
UpKey.irq (handler=IO_callback , trigger=UpKey.IRQ_RISING) 