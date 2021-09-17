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
    BLE.ScanConnect(name_header='EPY_') # scan and select the name have 'EPY_' header and most near device (scan 5sec)
    BLE.ScanConnect(mac='7002000008B6') # don't need scan , use device mac address connect
V1.000 = first release version    
V1.001 
    - fixed mac connect change data mode
V1.002 
    - fixed data receve return issues
    - fixed change ROLE check message error

"""
from machine import delay

class GATT:
    
    def __init__(self, uart, role='PERIPHERAL'):
        self.ROLE = ''
        self.MODE = ''
        self.state = 'DISCONNECTED'
        self.ble = uart
        self.ChangeMode('CMD')
        self.msg_on() #enable system message
        self.ChangeRole(role)
        
    def writeCMD_respons(self, atcmd,datamode =True):
        if self.MODE == 'DATA':
            self.ChangeMode('CMD')
        self.ble.write(atcmd+'\r\n')
        delay(50)
        msg = self.ble.read(self.ble.any())
        if 'SYS-MSG: CONNECTED OK' in msg:
            self.state = 'CONNECTED'
        elif 'SYS-MSG: DISCONNECTED OK' in msg:
            self.state = 'DISCONNECTED' 
        if datamode == True:
            self.ChangeMode('DATA')
        return(msg)

    def ChangeMode(self, mode):
        if self.MODE ==  '' :
            msg = ''
            while "OK" in msg:
                self.ble.write('!CCMD@')
                delay(200)
                self.ble.write('AT\r\n')
                delay(50)
                msg = self.ble.read(self.ble.any())
            self.MODE = 'CMD'
        if mode == self.MODE:
            return
        elif mode == 'CMD':
            delay(150)
            self.ble.write('!CCMD@')
            delay(150)
            msg = self.ble.readline()
            
            while not 'SYS-MSG: CMD_MODE OK' in msg:
                msg = self.ble.readline()
                
                delay(50)
            self.MODE = 'CMD'
        elif mode == 'DATA':
            self.ble.write('AT+MODE_DATA\r\n')
            delay(200)
            msg = self.ble.readline()
            
            while not 'SYS-MSG: DATA_MODE OK' in msg:
                msg = self.ble.readline()
                
                delay(50)
            self.MODE = 'DATA'
 
    def SendData(self, data):
        self.ble.write(data)
        return

    def RecvData(self):
        msg = self.ble.readline()

        if len(msg)> 0:
            if 'SYS-MSG: CONNECTED OK' in msg:
                self.state = 'CONNECTED'
                msg =''
            elif 'SYS-MSG: DISCONNECTED OK' in msg:
                self.state = 'DISCONNECTED'
                msg =''
            else :
                return (str(msg,'utf-8'))
        return (str(msg,'utf-8'))

    def ChangeRole(self, role):
        msg = self.writeCMD_respons('AT+ROLE=?')
        if 'PERIPHERAL' in msg:
            self.ROLE = 'PERIPHERAL'
        elif 'CENTER' in msg:
            self.ROLE = 'CENTER'
            
        if role == self.ROLE:
            return
        else:
            self.ChangeMode('CMD')
            if role == 'PERIPHERAL':
                self.ble.write('AT+ROLE=P\r\n')
            else : 
                self.ble.write('AT+ROLE=C\r\n')
            delay(500)
            msg = self.ble.readline()
            while 'READY OK' not in msg:
                msg = self.ble.readline()
            msg = self.ble.readline()
            
            self.ROLE = role
            self.ChangeMode('DATA')
            return (msg)
           
    def msg_on(self,en=1):
        msg = self.writeCMD_respons('AT+EN_SYSMSG={}'.format(en))
        return (msg)
        
    def ScanConnect(self,mac='',name_header ='EPY_'):
        device =[]
        if mac =='':
            while len(device) == 0:
                self.writeCMD_respons('AT+SCAN',datamode = False)
                delay(5000)
                msg = str(self.ble.readline(),'utf-8')
                while 'SCAN_END_DEV_NUM' not in msg and name_header in msg:
                    device.append(msg.split(' '))
                    msg = str(self.ble.readline(),'utf-8')
               
            sorted(device,key =lambda x:x[3]) 
           
            msg = self.writeCMD_respons('AT+CONN={}'.format(device[0][0]),datamode = True)
        else :
            msg = self.writeCMD_respons('AT+CONN={}'.format(mac),datamode = True)
            
        for i in range(10):
            msg = self.RecvData()
            if self.state == 'CONNECTED':
                break
            delay(200)
        return   
        
    def disconnect(self):
        msg = self.writeCMD_respons('AT+DISC',datamode = True)
        for i in range(10):
            msg = self.RecvData()
            if self.state == 'DISCONNECTED':
                break
            delay(200)
        return
      
            
            
