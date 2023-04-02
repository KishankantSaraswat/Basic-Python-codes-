num=int(input("Enter the number"))
sum=0
i=2
while num>=i:
    if num%i==0:
        sum=sum+i
if sum==num:
    print("is a perfect number")  
else:
    print("is not a perfect number")      