x=int(input("enter the number"))
y=0
while x>0:
    digit=x%10
    y=y*10+digit
    x=x//10
    print("reversed of given number=",y)