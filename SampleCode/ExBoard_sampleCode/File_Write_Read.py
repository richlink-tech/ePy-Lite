
# 開啟一可寫入檔案 ，檔名 'ePyLite.txt' , 不管檔案存不存在 都由最前頭寫入, 純文字檔
fileA = open ('ePyLite.txt','w')
fileA.write ('I am ePy Lite Board.\r\n') # 寫入檔案內容 , \r\n 換行
fileA.write ('This is a file write and read sample.\r\n')
fileA.close() #強制將最後的資料寫入

#開啟剛剛的檔案，設定讀取
f = open ('ePyLite.txt','r')
file_text = f.read() #讀出所有內容
print (file_text)
f.close