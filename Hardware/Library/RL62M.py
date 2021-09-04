"""
RL62M is UART AT command module ,baudrate = 115200
It can be set to PERIPHERAL(Server / Device ) mode.
also , It can be set to Center mode( Client / Master ) mode

How to use the Library

from machine import *
import RL62M 
uart = UART(1,115200,timeout=200,read_buf_len=512)
BLE = RL62M.GATT(uart,role='PERIPHERAL') or 'CENTER'

PERIPHERAL/CENTER Mode -- 
    msg = BLE.RecvData() : recv data and check connect/disconnect status , msg is string type(UTF-8)
    BLE.SendData('ABC')
CENTER Mode -- 
    BLE.ScanConnect() # scan and select the most near device (scan 5sec)
    BLE.ScanConnect(mac='7002000008B6') # don't need scan , use device mac address connect

"""
from machine import delay
class GATT:
    def __init__(self, uart, role='PERIPHERAL'):
        self.ROLE = ''
        self.MODE = ''
        self.state = 'DISCONNECTED'
        self.ble = uart
        self.msg_on() #enable system massage
        self.ChangeRole(role)
 
    def writeCMD_respons(self, atcmd,datamode =True):
        if self.MODE == 'DATA':
            self.ChangeMode('CMD')
        self.ble.write(atcmd+'\r\n')
        delay(50)
        msg = self.ble.read(self.ble.any())
        if datamode == True:
            self.ChangeMode('DATA')
        return(msg)

    def ChangeMode(self, mode):
        if mode == self.MODE:
            return
        elif mode == 'CMD':
            msg = ''
            while not 'OK' in msg:
                self.ble.write('!CCMD@')
                delay(200)
                self.ble.write('AT\r\n')
                delay(50)
                msg = self.ble.read(self.ble.any())
                
            
            self.MODE = 'CMD'
        elif mode == 'DATA':
            self.ble.write('AT+MODE_DATA\r\n')
            delay(200)
            msg = self.ble.read(self.ble.any())
            self.MODE = 'DATA'
 
    def SendData(self, data):
        self.ble.write(data)
        return

    def RecvData(self):
        msg = self.ble.readline()
        if len(msg)> 0:
            if 'SYS-MSG: CONNECTED OK' in msg:
                self.state = 'CONNECTED'
            elif 'SYS-MSG: DISCONNECTED OK' in msg:
                self.state = 'DISCONNECTED'
            else :
                return (str(msg,'utf-8'))
        else:
            return (None)

    def ChangeRole(self, role):
        if role == self.ROLE:
            return
        else:
            self.ChangeMode('CMD')
            if role == 'PERIPHERAL':
                self.ble.write('AT+ROLE=P\r\n')
            else : 
                self.ble.write('AT+ROLE=C\r\n')
            delay(500)
            msg = self.ble.read(self.ble.any())
            self.ROLE = role
            self.ChangeMode('DATA')
            return (msg)
           
    def msg_on(self,en=1):
        self.ChangeMode('CMD')
        self.ble.write('AT+EN_SYSMSG={}\r\n'.format(en))
        delay(50)
        msg = self.ble.read(self.ble.any())
        self.ChangeMode('DATA')
        return (msg)
        
    def ScanConnect(self,mac=''):
        device =[]
        if mac =='':
            self.writeCMD_respons('AT+SCAN',datamode = False)
            delay(5000)
            msg = str(self.ble.readline(),'utf-8')
            
            while 'SCAN_END_DEV_NUM' not in msg and 'EPY_' in msg:
                device.append(msg.split(' '))
                msg = str(self.ble.readline(),'utf-8')
               
            sorted(device,key =lambda x:x[3])
            #print (device)
            msg = self.writeCMD_respons('AT+CONN={}'.format(device[0][0]))
        else :
            msg = self.writeCMD_respons('AT+CONN={}'.format(mac))
        for i in range(20):
            msg = self.RecvData()
            if self.state == 'CONNECTED':
                break
            delay(100)
        return (self.state)   
           
