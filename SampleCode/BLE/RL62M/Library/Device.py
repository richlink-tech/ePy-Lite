'''
Create a BLE server (PERIPHERAL mode)

  BLE.RecvData() is recv data and check BLE system message for connect or disconnect
  recv data is 'A'  Lite will toggle the (Y)LED on lite board
  Alaway send the string "ABC" to CENTER (Mobile phone or Client)
'''

from machine import *
import RL62M 
uart = UART(1,115200,timeout=200,read_buf_len=512)
ledy = LED('ledy')

''' PERIPHERAL Mode sample '''
BLE = RL62M.GATT(uart,role='PERIPHERAL')
while True: # wait be connected
    BLE.RecvData()
    if BLE.state == 'CONNECTED':
        #print('connected')
        break
    else :
        #print('wait-',end='')
        delay(100)
while True: # send / recv data
    m=BLE.RecvData()
    if BLE.state == 'DISCONNECTED':
        #print('disconnected')
        break
    else :
        BLE.SendData('ABC')
        if m != None :
            if m == 'A':
              ledy.toggle()
            #print ('recv data is:' , m)
    delay(100)
