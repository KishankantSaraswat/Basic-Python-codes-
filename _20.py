num=int(input("Enter the number:"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit*digit*digit
    temp=temp//10
    if sum==num:
        print(num,"is a Armstrong Number ",end="")
    else:
        print(num,"is NOT a Armstrong Number ")

