# ePy Lite use Pin.board.P13
from machine import DHT11,delay
dht=DHT11(0)
print ('temperature and humidity: ',dht.read())
delay(500)
print ('temperature: ', dht.read_temperature())
delay(500)
print ('temperature and humidity: ',dht.read_humidity())
