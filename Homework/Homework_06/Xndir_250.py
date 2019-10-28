a=[1,5,8,4.2,1,10,1,1,9.2,1,3.3,]
b=1
i=0

for i in range(0,len(a)):
    if (i*a[i])%3==2:
        b=b*a[i]**2
print(b)
