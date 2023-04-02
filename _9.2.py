import math as M
num=int(input("Enter the number:"))
t=num
sum=0
#seprate the digits 
while t>0:
   rem=t%10
   t=t//10
   
   fact=1
   fact=M.factorial(rem)
 
   
   sum=fact+sum
if sum==num:
    print("this is a krishanmurthy number")
else:
    print("this is not a krishanmurthy number")