import math
x=int(input())
k=[2,3,4,5,6,7,8]

def func_if(x,k):
    for i in k:
        y=9*x**i
        i=i+1
        print("y="+str(y))


def func_else(x,k):
    for i in k:
        y=8*x+i**3
        i=i+1
        print("y="+str(y))

if x>3 and x<7:
    func_if(x,k)

else:
    func_else(x,k)


