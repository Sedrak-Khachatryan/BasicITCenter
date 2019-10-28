a=[[1,2,3,4,5],[10,15,20,25,30],[3,6,9,12,15],[2,4,6,8,10],[2,3,5,6,7],]
x=0
for i in range(len(a)):
    for j in range(len (a[i])):
        if i==j:
            x=x+a[i][j]
print(x)