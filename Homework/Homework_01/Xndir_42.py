import math
x=float(input())
y=float(input())
if (-1<=x<=-0.5 or 0.5<=x<=1 ) and (-1<=y<=-0.5 or 0.5<=y<=1):
    z=x+math.pow(y,2)
    print(z)
else:
    z=5*x
    print(z)