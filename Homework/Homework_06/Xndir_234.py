a=[1,5,6,8,9,11,5,-5,15,-2,1,8,88]
b=0
c=0
for i in a:
    if i/2!=i/2-i%2:
        b=b+i
        c=c+1
print(b/c)