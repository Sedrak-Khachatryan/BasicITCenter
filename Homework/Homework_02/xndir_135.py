x=int(input())
k=[1,2,3,4]

def func_1(x,k):
    for i in k:
        y=x**(i-1)
        print(y)

def func_2(x,k):
    for i in k:
        y=x*i**3
        print(y)
if x>1:
    func_1(x,k)
elif x<3:
    func_2(x,k)
else:
    y=10**(-6)
    print(y)
