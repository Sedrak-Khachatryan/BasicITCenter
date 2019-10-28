import math
a=[0,12,15,18,19,99,98,-10,-60,-80,-30]
k=25
b=0
for i in range(0,len(a)):
    if math.fabs(a[i]-i)>k:
        b=b+1
print(b)