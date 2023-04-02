#Range of perfect number
import math as M
print("Enter a range to find Perfect number")
Range1=int(input("from:"))
Range2=int(input("to:"))
for num in range(Range1,Range2+1):
    
    sum=0
    i=2
while num>=i:
    if num%i==0:
        sum=sum+i
if num==sum:
    print(num)
