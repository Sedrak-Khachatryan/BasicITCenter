import random
n=int(input("n= "))
a=0
arr=[[random.randint(-100,100) for i in range(n)]for j in range(n)]
print(arr)
m=int(input("Ojandak ankjunagci vra hashvelu hamar mutqagrel - 1 \nojandak ankjunagcic nerqev hashvelu hamar - 2"))
if m==1:
    for i in range(n):
        for j in range(n):
            if i+j==n-1:
                if (i+j)%2!=0:
                    a=a+1
    print(a)
elif m==2:
    for i in range (1,n):
        for j in range(n-i,n):
            if (i+j)%2!=0:
                a=a+1
    print(a)