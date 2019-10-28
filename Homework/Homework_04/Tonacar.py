a=int(input())
c="* "
if a>0:
    print(c.center(a*2))
for i in range(0,a):
    if i>0:
        c=c+"* "
        print(c.center(a*2))