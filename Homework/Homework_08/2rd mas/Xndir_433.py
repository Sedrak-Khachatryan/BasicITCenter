import random
n=int(input("n= "))
print("Mutqagrel 'a'-i ev 'b'-i arjeqner@")
a=int(input("a= "))
b=int(input("b= "))
c=0
arr=[[random.randint(-100,100) for i in range(n)]for j in range(n)]
print(arr)
for i in range (0,n-1):
    for j in range(0,n-1-i):
        if arr[i][j]>=a and arr[i][j]<=b:
            c=c+1
print(c)