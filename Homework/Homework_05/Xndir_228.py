a=[-1,5,15,-5,9,100,-100,8,24,-40,3,0,88,-90]
b=len(a)
k=25
c=0
for i in range(0,len (a)):
    if i>0 and k/i==k/i-k%i:
        c=c+a[i]
print(c)
