#Range of neon number
print("Enter a range to find neon number")
Range1=int(input("from"))
Range2=int(input("to"))
for x in range(Range1,Range2+1):
    sqr=x*x
    sum_of_digit=0
    while sqr>0:
       sum_of_digit =sum_of_digit + sqr%10
       sqr = sqr//10
    if sum_of_digit==x:
       print(x,end="")