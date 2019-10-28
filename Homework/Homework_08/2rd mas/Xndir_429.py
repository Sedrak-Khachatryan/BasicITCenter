import random
m=int(input("m= "))
a=0
b=0
arr=[[random.randint(-100,100) for i in range(m)]for j in range(m)]
print(arr)
n=int(input("Glxavor ankyunagcic verev hashvelu hamar mutqagrel - 1\tGlxavor ankjunagci vra hashvelu hamar - 2"))
if n==1:
    for i in range (0,m-1):
        for j in range(i+1,m):
            if math.fabs(arr[i][j])%5==2:
                a=a+1
    print(a)
elif n==2:
    for i in range(m):
        for j in range (m):
            if math.fabs(arr[i][j])%5==2:
                b=b+1
    print(b)