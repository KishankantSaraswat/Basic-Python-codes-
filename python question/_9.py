x=int(input("Enter the number:"))
sqr=x*x
sum_of_digit=0
while sqr>0:
    sum_of_digit =sum_of_digit + sqr%10
    sqr = sqr//10
if (x==sum_of_digit):
    print("this is Neon Number")
else:
    print("this is not a Neon Number")