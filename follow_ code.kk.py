import time
from random import randint

for i in range(1,45):
    print('')
s=''
for i in range (1,1000):
     count=randint(1,1000)
     while(count>0):
         s+=1
         count-=1
         if (i%10==0):
             print(s+'follow @coder.kk')
         else:
            print(s+'*')
         s=''
         time.sleep(0.3)
                   
