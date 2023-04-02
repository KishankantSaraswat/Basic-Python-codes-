x=int(input("Enter the number"))
resversed_num=0
while x>0:
    digit=x%10
    resversed_num=resversed_num*10+digit
    x=x//10
    print("resversed of given number",resversed_num,end="")
