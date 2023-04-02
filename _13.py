#Python str () Function 
# str () function converts the specified value into a string.
def decimal_to_binary(n):
    
    if n>1:
        decimal_to_binary(n//2)
    print(n%2,end="")