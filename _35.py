num=int(input("Enter the number:"))
reverse=int(str(num)[::-1])
print("reversed string:",reverse)
if num==reverse:
    print("given number is palindrome number")
else:
    print("not palindrome")