
# RL62M Module Class Library
RL62M01 is a BLE V5.0 AT CMD Module ，It be builded in ePy Lite (Micropython Board). It is very easy use in small MCU application

You can download the datasheet and AT command programming guide from the website

https://www.richlink-tech.com/%E8%B3%87%E6%96%99%E4%B8%8B%E8%BC%89 

## How to use the sample code 
> A1. Use keyA on ePy-Lite Board into USB Mass-Storage 
> 
> A2. copy the Device.py to EASYPY disk ,and rename to main.py
> 
> - **Other ePy-Lite Board**
> 
> B1. Use keyA on other ePy-Lite Board into USB Mass-Storage 
> 
> B2. copy the Master.py to EASYPY disk ,and rename to main.py
> 
> 3. reset two ePy-Lite system
> 
> 4. about 6-8 sec , you will see the BLE Blue LED on , and Y LED Toggle (1sec) 

## Class API 
### Creat a BLE GATT module object
- RL62M.GATT ( uart port , role = 'role mode')
> uart port : baudrate = 115200/8-N-1
> 
> role have two mode :  
>   - 'PERIPHERAL' : Server (Device) Mode ，Passive connection
>   - 'CENTRAL' : Client (Master) Mode ，Active connection

micropython example :
```python
uart = UART(1,115200,timeout=200,read_buf_len=512)
BLE = RL62M.GATT(uart,role='PERIPHERAL')
```
### CENTRAL Mode Scanning and Connect to Device 
- BLE.ScanConnect(name_header = 'EPY_ ') : auto scanning the device and connect to first device by sorted RSSI (need 5 sec to scanning)
- BLE.ScanConnect(mac='mac address') : Direct connect to the mac address device , mac address 70:02:00:00:08:B6 , use '7002000008B6'

example 
```python
BLE.ScanConnect(name_header = 'EPY_ ') # scan and select the BLE name have 'EPY_' header and most near device (scan 5sec)
BLE.ScanConnect(mac='7002000008B6')
```
### Send Data API
- BLE.SendData(string) : send the string data 

example 
```python
BLE.SendData('ABC')
BLE.SendData('ABC\r\n')
BLE.SendData('my name is {}'.format('Wright') )
```
### Receive  Data API
- msg = BLE.RecvData() : return the string data (UTF-8)

example 
```python
m=BLE.RecvData()
```
### Connect status
- BLE.state : 'CONNECTED' / 'DISCONNECTED'
The State will change use BLE.RecvData() API

### Disconnect
- BLE.disconnect()
