def neon(x):
    sqr=num*num
    sum=0
    while sqr>0:
        sum=sum+sqr%10
        sqr=sqr//10

    if (num==sum):
        print("neon number")
    else:
        print("not neon number")

num=int(input("enter the number"))
neon(num)