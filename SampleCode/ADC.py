
from machine import ADC,Pin

adc0 = ADC(Pin.epy.AIN0)
adc1 = ADC(Pin.epy.AIN1)
adc2 = ADC(Pin.epy.AIN2)
adc3 = ADC(Pin.epy.AIN3)
adc4 = ADC(Pin.epy.AIN4)
adc5 = ADC(Pin.epy.AIN5)


while True:
    print ('ADC0=',adc0.read())
    machine.delay(1)
    print ('ADC1=',adc1.read())
    machine.delay(1)
    print ('ADC2=',adc2.read())
    machine.delay(1)
    print ('ADC3=',adc3.read())
    machine.delay(1)
    print ('ADC4=',adc4.read())
    machine.delay(1)
    print ('ADC5=',adc5.read())
    machine.delay(100)

