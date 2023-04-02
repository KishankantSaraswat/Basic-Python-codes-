str1=input("enter string")
str2=input("enter substring")
if str1.find(str2)==-1:
    print("Substring not found in string")
else:
    print("substring is present")