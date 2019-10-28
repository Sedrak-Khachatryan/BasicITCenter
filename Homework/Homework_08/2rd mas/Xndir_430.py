import random
n=int(input("n= "))
a=0
b=0
arr=[[random.randint(-100,100) for i in range(n)] for j in range(n) ]
print(arr)
m=int(input("Glxavor ankyunagcic nerqev hasvelu hamar mutqagrel - 1\nGlxavor ankyunagci vra hashvelu hamar - 2"))
if m==1:
    for i in range(1,n):
        for j in range(0,i):
            if arr[i][j]%2==0:
                a=a+arr[i][j]
                b=b+1
    print(a/b)
elif m==2:
    for i in range(n):
        for j in range(n):
            if arr[i][j]%2==0:
                a=a+arr[i][j]
                b=b+1
    print(a/b)