from machine import Switch,UART,LED,Pin,delay
import RL62M
Light_MAC_Address= '655700001064'
BLE_Light_NAME = 'RL-EPY-LIGHT_'
led = LED('ledy')
key = Switch('keya')
uart1 = UART(1,115200,timeout=300)
Light_CMD = [0x87,0x01,0x00,0x09,0x00,0x00,0x00,0x00,0x00,0x00,0x0F,0x0F,0x00]
'''Command Header 3 byte, Length 1 byte ,4 byte Reserve#  +  C,W,R,G,B'''
def LightColor(C,W,R,G,B):
    global Light_CMD
    Light_CMD[8] = C
    Light_CMD[9] = W
    Light_CMD[10] = R
    Light_CMD[11] = G
    Light_CMD[12] = B
    BLE.SendData(bytearray(Light_CMD))
    delay(100)
def key_func():
    global KeyTimes
    KeyTimes =KeyTimes+1
    if KeyTimes >=6 :
        KeyTimes = 0
KeyTimes = 0
key.callback(key_func)
BLE = RL62M.GATT(uart1,role='CENTRAL') 
BLE.ScanConnect(mac=Light_MAC_Address)
while True:
    if KeyTimes == 0:
        LightColor (255,0,0,0,0) # Cool Color LED
    elif KeyTimes == 1:
        LightColor (0,255,0,0,0) # Warm Color LED
    elif KeyTimes == 2:
        LightColor (0,0,255,0,0) # Red Color
    elif KeyTimes == 3:
        LightColor (0,0,0,255,0) # Yellow Color
    elif KeyTimes == 4:
        LightColor (0,0,0,0,255) # Blue Color
    elif KeyTimes == 5: 
# change RGB data to do the Rainbow show 
        while True:
            for color in range(1,255,10):
                LightColor (0,0,color,0,255)
                if KeyTimes != 5:
                    break
            for color in range(255,0,-10):
                LightColor (0,0,255,0,color)
                if KeyTimes != 5:
                    break
            for color in range(1,255,10):
                LightColor (0,0,255,color,0)
                if KeyTimes != 5:
                    break
            for color in range(255,0,-10):
                LightColor (0,0,color,255,0)
                if KeyTimes != 5:
                    break
            for color in range(1,255,10):
                LightColor (0,0,0,255,color)
                if KeyTimes != 5:
                    break
            for color in range(255,0,-10):
                LightColor (0,0,0,color,255)
                if KeyTimes != 5:
                    break
            if KeyTimes != 5:
                break    




