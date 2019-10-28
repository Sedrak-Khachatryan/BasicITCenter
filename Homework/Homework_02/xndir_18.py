import math
x=float(input())
z=float(input())
if x>=1 and x<=7:
    y=math.pow((x+2*z),1/4)+math.e**(x+1)
    print(y)

else:
    y=math.tan((x+z)**7)**2
    print(y)

