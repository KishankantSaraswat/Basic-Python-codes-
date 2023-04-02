'''import math as M
x=int(input("Enter the number:"))
fact=1
factorial=M.factorial(x)
print(factorial)'''

x=int(input("Enter the number:"))
fact=1
i=1
while i<=x:
    fact=fact*i
    i=i+1
    print("the factorial of the number %d is %d" %(x,fact))
