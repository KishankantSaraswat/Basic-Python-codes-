row= int(input("ENTER NUMBER OF ROWS"))
col=int(input("ENTER NUMBER OF COLUMNS"))
ls=[]
for i in range(row):
    ls1=[]
    for j in range(col):
        x=int(input())
        ls1.append(x)
    ls.append(ls1)
for i in range(row):
    for j in range(col):
        print(ls[i][j],end =" ")
    print()
for i in range(row):
    for j in range(col):
        if (i==j):
            print( "daigonal",ls[i][j],end =" ")
    print()
print("secondary diagonal:")
for i in range(row):
    for j in range(col):
        if i+j==(row-1):
            print( "daigonal",ls[i][j],end =" ")
    print()
    
    

