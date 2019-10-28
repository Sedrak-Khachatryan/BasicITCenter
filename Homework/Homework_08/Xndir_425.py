import random
m=int(input("m= "))
a=0
arr=[[random.randint(-100,100) for i in range(m)]for j in range(m)]
print(arr)
for i in range(1,m):
    for j in range(0,i):
        if j<i:
            if arr[i][j]%2==0.0:
                a=a+1
print(a)
