
# 'a' 附加到原有檔案後面
with open ('ePyLite.txt','a') as fileA:
    fileA.write ('Line 3\r\n') # 寫入檔案內容 , \r\n 換行
    fileA.write ('Line 4\r\n')

#開啟剛剛的檔案，設定讀取
with open ('ePyLite.txt','r') as f:
    for i in range(10):
        file_text_line = f.readline() #讀出第一行
        print (file_text_line,end='') #不換行

    
