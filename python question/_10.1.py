#Range of Krishnmurthy  number
import math as M
print("Enter a range to find krishanmurthy number")
Range1=int(input("from:"))
Range2=int(input("to:"))
for x in range(Range1,Range2+1):
    import math as M

    t=x
    sum=0
#seprate the digits 
    while t>0:
        rem=t%10
        t=t//10
        i=1
        fact=1
        fact=M.factorial(rem)
        sum=fact+sum
        if sum==x:
            print(x)
