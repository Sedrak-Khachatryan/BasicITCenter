x=int(input())
k=[1,2,3,4]

def func_1(x,k):
    for i in k:
        y=3*x**(i+1)
        print(y)



def func_2(x,k):
    for i in k:
        y=5*x+i**7
        print(y)

if x>1:
    func_1(x,k)
else:
    func_2(x,k)

