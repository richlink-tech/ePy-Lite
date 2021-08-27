from machine import LED,delay,Pin

ledy = LED('ledy')

def pin_callback_fun(pin):
    ledy.toggle()
    
p0 = Pin(Pin.epy.P0,Pin.OUT) # P0 Output GPIO
p1 = Pin(Pin.epy.P1,Pin.IN)  #P1 Input GPIO

key = Pin.epy.KEYA
#IRQ_RISING,Pin.IRQ_FALLING , IRQ_HIGH , IRQ_LOW
key.irq(handler=pin_callback_fun , trigger=key.IRQ_FALLING) 

while True:
    p0.value(1) # Output High
    print ('P0 output High')
    print ('P1 input is {}'.format(p1.value()))
    delay(500)
    p0.value(0) # Output Low
    print ('P0 output Low')
    print ('P1 input is {}'.format(p1.value()))
    delay(500)
