import math
a=[-8,3,10,-5,5,-25,7,44,-99]
x=0
y=0
for i in a:
    if i<0:
        x=x+i**2
        y=y+1
print(math.sqrt(x/y))
