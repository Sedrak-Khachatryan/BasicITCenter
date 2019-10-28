import math
x=int(input())
k=[2,3,4,5,6,7]
if x<6:
    for i in k:
        y=x**i+i**6
        i=i+1
        print("y="+str(y))

else:
    for i in k:
        y=math.log(i,5)
        i=i+1
        print("y="+str(y))
