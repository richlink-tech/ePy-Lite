"""
RL62M is UART AT command module ,baudrate = 115200
It can be set to PERIPHERAL(Server / Device ) mode.
also , It can be set to CENTRAL mode( Client / Master ) mode
How to use the Library
from machine import *
import RL62M
uart = UART(1,115200,timeout=200,read_buf_len=512)
BLE = RL62M.GATT(uart,role='PERIPHERAL') or 'CENTRAL'
PERIPHERAL/CENTRAL Mode --
    msg = BLE.RecvData() : recv data and check connect/disconnect status , msg is string type(UTF-8)
    BLE.SendData('ABC')
CENTRAL Mode --
    BLE.ScanConnect() # scan and select the most near device (scan 5sec)
    # don't need scan , use device mac address connect
    BLE.ScanConnect(mac='7002000008B6')
V1.000 = first release version
V1.001
    - fixed mac connect change data mode
V1.002
    - fixed data receve return issues
    - fixed change ROLE check message error
V1.004 (2021.9.27)
    - use utime for delay
    - tested by Raspberry Pi Pico uart0

"""
from utime import sleep_ms as delay
import utime


class GATT:

    def __init__(self, uart, role='PERIPHERAL'):
        self.ROLE = ''
        self.MODE = ''
        self.state = 'DISCONNECTED'
        self.Adv_Interval_ms = 200
        self.AdvState = 1
        self.AdvScanState = 0
        self.ble = uart
        self._init_RL62M()
        self.ChangeRole(role)

    def __del__(self):
        self.ble.deinit()

    ''' init RL62M to Command mode and enable sysmsg'''

    def _init_RL62M(self):
        delay(500)
        msg = ''
        while "OK" not in msg:
            self.ble.write('!CCMD@')
            delay(200)
            self.ble.write('AT\r\n')
            delay(50)
            msg = self.ble.read(self.ble.any())
            if msg == None:
                msg = ''
        self.MODE = 'CMD'
        msg = self.WriteCMD_withResp('AT+EN_SYSMSG=?', timeout=1000)

        if "EN_SYSMSG 0" in msg:
            msg = self.WriteCMD_withResp('AT+EN_SYSMSG=1', timeout=1000)

        msg = self.ble.read(self.ble.any())   # Clear all UART Buffer

    def writeCMD_respons(self, atcmd, datamode=True):
        if self.MODE == 'DATA':
            self.ChangeMode('CMD')
        self.ble.write(atcmd+'\r\n')
        delay(50)
        msg = self.ble.read(self.ble.any())
        if msg == None:
            msg = ''
        if 'SYS-MSG: CONNECTED OK' in msg:
            self.state = 'CONNECTED'
        elif 'SYS-MSG: DISCONNECTED OK' in msg:
            self.state = 'DISCONNECTED'
        if datamode == True:
            self.ChangeMode('DATA')
        return(msg)

    def WriteCMD_withResp(self, atcmd, timeout=50):
        self.ChangeMode('CMD')
        self.ble.write(atcmd+'\r\n')
        prvMills = utime.ticks_ms()
        resp = b""
        while (utime.ticks_ms()-prvMills) < timeout:
            if self.ble.any():
                resp = b"".join([resp, self.ble.read(self.ble.any())])
                #print('rep-', atcmd, resp, utime.ticks_ms()-prvMills)
            delay(100)
        return (resp)

    def ChangeMode(self, mode):
        if mode == self.MODE:

            return
        elif mode == 'CMD':
            delay(150)
            self.ble.write('!CCMD@')
            delay(200)
            msg = self.ble.readline()
            if msg == None:
                msg = ''
            while not 'SYS-MSG: CMD_MODE OK' in msg:
                msg = self.ble.readline()
                if msg == None:
                    msg = ''
                delay(50)
            self.MODE = 'CMD'
        elif mode == 'DATA':
            msg = self.WriteCMD_withResp('AT+MODE_DATA', timeout=600)
            while not 'SYS-MSG: DATA_MODE OK' in msg:
                print('change to data mode fail')
                delay(100)
            self.MODE = 'DATA'
        else:
            pass

    def SendData(self, data):
        self.ChangeMode('DATA')
        self.ble.write(data)
        return

    def RecvData(self):
        msg = self.ble.readline()
        if msg == None:
            msg = ''
        if len(msg) > 0:
            if 'SYS-MSG: CONNECTED OK' in msg:
                self.state = 'CONNECTED'
                msg = ''
            elif 'SYS-MSG: DISCONNECTED OK' in msg:
                self.state = 'DISCONNECTED'
                msg = ''
            else:
                return (str(msg, 'utf-8'))
        return (str(msg, 'utf-8'))

    def ChangeRole(self, role):
        if self.ROLE == '':
            msg = self.WriteCMD_withResp('AT+ROLE=?', timeout=1000)

            if 'PERIPHERAL' in msg:
                self.ROLE = 'PERIPHERAL'
            elif 'CENTRAL' in msg:
                self.ROLE = 'CENTRAL'

        if role == self.ROLE:
            return
        else:

            if role == 'PERIPHERAL':
                msg = self.WriteCMD_withResp(
                    'AT+ROLE=P', timeout=2000)  # 2sec for epy ble v1.03

            else:
                msg = self.WriteCMD_withResp(
                    'AT+ROLE=C', timeout=2000)  # 2sec for epy ble v1.03
            if 'READY OK' not in msg:
                print('Change Role fail ;', msg)

            self.ROLE = role
            self.ChangeMode('DATA')
            return

    def ScanConnect(self, mac='', name_header='EPY_'):
        device = []
        if mac == '':
            while len(device) == 0:
                msg = str(self.WriteCMD_withResp(
                    'AT+SCAN', timeout=5000), 'utf-8')
                msg = msg. split('\r\n')
                for dev in msg:
                    sdev = dev.split(' ')
                    if len(sdev) == 5:
                        device.append(sdev)
            sorted(device, key=lambda x: int(x[3]), reverse=True)
            msg = self.WriteCMD_withResp(
                'AT+CONN={}'.format(device[0][0]), timeout=300)
        else:
            msg = self.WriteCMD_withResp(
                'AT+CONN={}'.format(mac), timeout=300)

        for i in range(10):
            msg = self.RecvData()
            if self.state == 'CONNECTED':
                self.ChangeMode('DATA')
                break
            delay(200)
        return

    def disconnect(self):
        msg = self.WriteCMD_withResp('AT+DISC', timeout=200)
        for i in range(10):
            msg = self.RecvData()
            if self.state == 'DISCONNECTED':
                break
            delay(200)
        return

    def SetAdvInterval_ms(self, time_ms=200):
        # 50/100/200/500/1000/2000/5000/10000/20000/50000
        if time_ms != self.Adv_Interval_ms and self.ROLE == 'PERIPHERAL':
            msg = self.WriteCMD_withResp('AT+ADV_INVTERVAL={}'.format(time_ms))
            if "OK" in msg:
                self.Adv_Interval_ms = time_ms
        return

    def EnableAdvMode(self, enable=1):

        if enable != self.AdvState and self.ROLE == 'PERIPHERAL':
            msg = self.WriteCMD_withResp('AT+ADVERT={}'.format(enable))
            if "OK" in msg:
                self.AdvState = enable
        return

    def SetAdvData(self, data):
        send_data = ''
        if len(data) > 31:
            data = data[:31]
        #send_data = hex(len(data)+1)[2:]+'09'
        send_data = send_data.join([hex(ord(x))[2:] for x in data])

        send_data = hex(len(data)+1)[2:]+'09' + send_data

        msg = self.WriteCMD_withResp(
            'AT+AD_SET=0,{}'.format(send_data))
        return

    def EnableAdvScan(self, enable=1):
        if self.AdvScanState != enable and self.ROLE == 'CENTRAL':
            msg = self.WriteCMD_withResp(
                'AT+ADV_DATA_SCAN={}'.format(enable), timeout=1000)
            if "OK" in msg:
                self.AdvScanState = enable

    def AdvSendData(self, group='01', who_recv='0', data=''):
        send_data = ''
        if self.ROLE != 'PERIPHERAL':
            self.ChangeRole("PERIPHERAL")
        send_data = 'EPY-'+','+group+','+who_recv+','+data+','+'@@@'
        self.SetAdvData(send_data)
        self.EnableAdvMode(enable=1)

    def AdvRecvData(self, group='01', who='None'):
        str_data = ''
        if self.ROLE != 'CENTRAL':
            self.ChangeRole("CENTRAL")
        self.EnableAdvScan(enable=1)

        msg = ''
        while len(msg) < 1:
            msg = str(self.ble.readline(), 'utf-8')

            if len(msg) > 0:
                msg = msg.strip()
                msg = str(msg).split(' ')

                # check ADV_DATA and EPY- in ADV data
                if 'ADV_DATA' in msg[0] and '094550592D' in msg[3]:
                    msg = msg[3][4:]  # del lenth and 0x09
                    break
                else:
                    msg = ''
            delay(100)

        str_data = "".join(chr(int(msg[i:i+2], 16))
                           for i in range(0, len(msg), 2))
        str_data = str_data.split(',')
        # print(str_data)
        if 'EPY-' in str_data[0] and group == str_data[1]:
            if who == str_data[2]:
                return (str_data[3])
            elif who == '0':  # who = '0' is group msg
                return (str_data[3])
