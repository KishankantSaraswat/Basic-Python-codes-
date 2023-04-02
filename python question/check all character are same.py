str=input()
all_same=str==str*len(str)
print(all_same)
if all_same:
    print("all charcter are same")
else:
    print("not all characters in the string is same")