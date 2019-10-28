import math
x=-3.14
while x<3.14:
    y=(math.sin(x))**2+math.cos(x)
    print("x="+str(x))
    x=x+3.14/8
    print("y="+str(y))