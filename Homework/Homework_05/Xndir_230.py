import math
a=[1.5,4,5.4,10,85,9,5,-5,-5.5,7.9,2,-2,4]
k=100
c=0
d=0
for i in  a:
    if i>0 and k/int(i)==k/int(i)-k%int(i):
        c=c+i**2
        d=d+1
print(math.sqrt(c/d))