import math
x=float(input())
a=float(input())
b=float(input())
if -5>a+b:
    y=math.e**(a+x)*math.cos(a+x+b)**2
    print(y)
elif a+b>2:
    y=math.pow(math.atan(a+x),1/3)
    print(y)
else:
    y=a+b
    print(y)