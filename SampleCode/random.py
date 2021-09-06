'''
ePy Lite random number module
'''
import urandom as random
'''
urandom.getrandbits (nbit)
取nbit 的亂數 , 2^7 = 0~128
'''
def rand (a,b): # 產生數字a到 b的 亂數 
    return (random.getrandbits(7) %(b-a+1)+ a)

for i in range(0,10):
    print (rand (0,4)) #取 0到 4亂數

for i in range(0,10):
    print (rand (2,4)) #取 2到 4亂數
    
random.randinit(10,100) # get int number 10~100 random number
random.random() # get 0 to <1 float random number
random.randrange (1,7) # get int 1 to 6 random number 

L = [[1,0,0],[0,1,0],[0,0,1],[20,20,0],[30,20,40]]

random.choice (L) # from L list random choice a item
