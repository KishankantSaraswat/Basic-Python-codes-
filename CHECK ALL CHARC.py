s=input( )
s==len(s)*s[0]
if all([x==s[0] for x in s]):
    print("all the character are same")
