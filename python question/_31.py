a=int(input("total actual prize=c.p"))
b=int(input("total selling prize"))
if a>b:
    print("Loss=",a-b)
elif b>a:
    print("Profit=",b-a)
else:
    print("equal")
