import random
import math
n=int(input("Mutqagrel 1-ojandak ankyunagcic verev kam 2 - ojandak ankyunagci vra hashvelu hamar:"))
m=int(input("m= "))
k=int(input("k= "))
a=1
b=1
arr=[[random.randint(-100,100) for i in range(m)]for j in range(m)]
print(arr)
if n==1:
    for i in range(0,m-1):
        for j in range(0,m-1-i):
            if j>i:
                if arr[i][j]%k==0:
                    a=a*arr[i][j]
    print(a)
elif n==2:
    for i in range(m):
        for j in range(m):
            if i+j==m-1:
                if arr[i][j]%k==0:
                    b=b*arr[i][j]
    print(b)
