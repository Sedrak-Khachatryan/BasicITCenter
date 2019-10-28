a=[-1,0,2,1,3,4,5,6,7,8,9,10]
b=[23,-32,44,-4,5,-5,8,-9,10,1,0,2]
x=0
y=0
for i in a:
    if i!=0:
        x=x+i
        x_1=x+1
mij_a=x/x_1
for n in b:
    if n!=0:
        y=y+n
        y_1=y+1
mij_b=y/y_1
artadryal=mij_a*mij_b
print(artadryal)