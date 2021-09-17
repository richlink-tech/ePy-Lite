'''
Create a Master (Central Mode)
direct scan and connect to first (reference RSSI) device 
send 'A' to device (1sec)
and recv 'A' to change (Y)LED status
'''

from machine import *
import RL62M 
uart = UART(1,115200,timeout=200,read_buf_len=512)
ledy = LED('ledy')

''' Center mode  sample '''
BLE = RL62M.GATT(uart,role='CENTRAL')
# two connect mode ,select one connect to device 
BLE.ScanConnect(name_header='EPY_') # scan and select the most near device (scan 5sec)
# BLE.ScanConnect(mac='7002000008B6') # don't need scan , use device mac address connect
 
while True: # send / recv data
    m=BLE.RecvData()
    if BLE.state == 'DISCONNECTED':
        break
    else :
        BLE.SendData('A')
        if m != None :
          if 'A' in m:
            ledy.toggle()
            #print ('recv data is:' , m)
    delay(1000)
