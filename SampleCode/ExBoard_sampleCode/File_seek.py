#製作測試檔案
with open ('ePyLite.txt','w') as f:
    f.write('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')


#開啟剛剛的檔案，設定讀取
with open ('ePyLite.txt','r') as f:
    for i in range(3):
        text_5 = f.read(5) #讀出5個字
        print (text_5,end='') #不換行
        
    print ('')   #強制換行
    # 移動讀檔位置到 第十字處 
    f.seek(10) 
    text_10 = f.read(10) 
    print ('seek 10-->' , text_10)

    
