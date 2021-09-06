# V1.8 FW Release note

1. 新增DHT11 sensor (Pin.epy.P13)

	```python
	# ePy Lite use Pin.board.P13
	from machine import DHT11,delay
	dht=DHT11(0)
	print ('temperature and humidity: ',dht.read())
	delay(500)
	print ('temperature: ', dht.read_temperature())
	delay(500)
	print ('temperature and humidity: ',dht.read_humidity())

	```
2. 修改ultra sonic輸入pin設定及擴充成6組可使用(EPWM0)
	- Trigger Pin固定使用 P10,P11,P12,P13,P14,P15
	- Echo Pin 對應      P6 , P7, P8, P9,P16,P17
	- Unit is cm
	```python
	from machine import USonic,Pin
	import utime

	su0=USonic(0, Pin.epy.P15) # Echo pin is P17(fix) , Trig is P15
	su1=USonic(1, Pin.epy.P14) # Echo pin is P16(fix) , Trig is P14
	su2=USonic(2, Pin.epy.P13) # Echo pin is P9(fix) , Trig is P13
	su3=USonic(3, Pin.epy.P12) # Echo pin is P8(fix) , Trig is P12
	su4=USonic(4, Pin.epy.P11) # Echo pin is P7(fix) , Trig is P11
	su5=USonic(5, Pin.epy.P10) # Echo pin is P6(fix) , Trig is P10
	while True:
		print ('USonic 0 dist is :',round(su0.distance()))
		print ('USonic 1 dist is :',round(su1.distance()))
		print ('USonic 2 dist is :',round(su2.distance()))
		print ('USonic 3 dist is :',round(su3.distance()))
		print ('USonic 4 dist is :',round(su4.distance()))
		print ('USonic 5 dist is :',round(su5.distance()))
		utime.sleep_ms(1000)
		print ('--------------------------------------------')
		
	```
3.	Update Timer/PWM input capture function (fix bug)
4.	新增music module (fix Pin.epy.P15)
	```python
	import music
	music.play(['C4:4','D',E5:8])
	```
5.	修正soft_spi 問題，system print時增加判斷user是否使用uart1
6.	新增UUID_MAC output
7.	分離hardware i2c/spi and software i2c/spi
	- 增加 Software I2C Module (SWI2C) , Hardware I2C (I2C)
	- 增加 Software SPI Module (SWSPI)


