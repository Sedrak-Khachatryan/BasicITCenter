import math
a=[-1,5,15,-5,9,100,-100,8,24,-40,3,0,88,-90]
k=25
b=0
for i in a:
    if math.fabs(i)<k:
        b=b+i**3
print(b)
