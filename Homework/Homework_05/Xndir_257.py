a=[1,20,15,10,1,2,3,20]
b=0
for i in range(0,len(a)):
    if b<a[i]:
        b=a[i]
for a[i] in a:
    if a[i]==b:
        print(a[i])