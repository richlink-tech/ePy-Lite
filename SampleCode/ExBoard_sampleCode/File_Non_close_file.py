
# with 包覆起來的區域，不需要再使用 close()
with open ('ePyLite.txt','w') as fileA:
    fileA.write ('I am ePy Lite Board.\r\n') # 寫入檔案內容 , \r\n 換行
    fileA.write ('This is a file write and read sample.\r\n')

#開啟剛剛的檔案，設定讀取
with open ('ePyLite.txt','r') as f:
    file_text_line1 = f.readline() #讀出第一行
    file_text_line2 = f.readline() #讀出第二行
    print (file_text_line2)
    print (file_text_line1)
    
