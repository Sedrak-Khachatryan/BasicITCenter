import random
m=int(input("m="))
k=int(input("k="))
a=[[random.randint(-100,100) for i in range(m) ]for j in range(m)]
print (a)
for i in range(1,m):
    for j in range(0,i):
        if j<i:
            if a[i][j]%k==0.0:
                print(a[i][j],end="\t")

