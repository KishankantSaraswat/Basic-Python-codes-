num=int(input("Enter the number"))
i=1
fact=1
while num>=i:
    fact=fact*i
    i=i+1
    print("The factorial of %d is %d",fact)