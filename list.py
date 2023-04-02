row= int(input())
col=int(input())
ls=[]
for i in range(row):
    for j in range(col):
        ls1=[]
        x=int(input())
        ls1.append(x)
    ls.append(ls1)
for i in range(row):
    for j in range(col):
        print(ls[i][j],end="")   