import random
m=int(input())
a=0
arr=[[random.randint(-100,100) for i in range(m)]for j in range (m)]
print(arr)
for i in range(0,m-1):
    for j in range(0,m-1-i):
        if j>i:
            if arr[i][j]%2==0.0:
                a=a+arr[i][j]
print(a)