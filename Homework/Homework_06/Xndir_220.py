a=[0,-1,-3,-4,100,66,95,5,9,10]
x=0
y=0
for i in range(0,len(a)):
    if a[i]>0:
        x=x+1
for i in range (0,len(a)):
    if a[i]<0:
        y=y+1
print("drakan arjeqneri qanak@ havasar e`"+str(x))
print("bacasakan arjeqneri qanak@ havasar e`"+str(y))
