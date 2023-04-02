p=float(input("Enter principal Amount:"))
t=float(input("Number of times interest is compounded per year:"))
r=float(input("Rate of interest per annum:"))
a=p*(1+r/100)**t
print("Amount after n years",a)

