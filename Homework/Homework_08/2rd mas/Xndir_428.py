import random
m=int(input("m= "))
a=0
b=0
arr=[[random.randint(-100,100) for i in range(m)]for j in range(m)]
print(arr)
n=int(input("Ojandak ankyunagci vra hashvelu hamar mutqagrel - 1 , ojandak ankyunagcic verev - 2"))
if n==1:
    for i in range (m):
        for j in range(m):
            if i+j==m-1:
                if arr[i][j]==0:
                    a=a+1
    print(a)
elif n==2:
    for i in range(0,m-1):
        for j in range(0,m-1-i):
            if j>i:
                if arr[i][j]==0:
                    b=b+1
    print(b)