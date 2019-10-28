x=[-1,0,2,1,3,4,5,6,7,8,9,10]
a=0
for i in range(0,len(x)):
    if i/2==i/2-i%2:
        a=a+x[i]

y=[23,-32,44,-4,5,-5,8,-9,10,1,0,2]
b=0
for i in range(0,len(x)):
    if i/2==i/2-i%2:
        b=b+y[i]

print(a+b)