import math
a=[1,2,3,4,-5,8,-9,0,3,2,15,99]
b=0
c=0
for i in range(0,len(a)):
    if i<a[i]:
        b=b+a[i]
        c=c+1
print(math.sqrt(b/c))