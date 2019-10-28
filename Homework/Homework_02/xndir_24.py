a=int(input())
b=int(input())
c=int(input())
if (a==2 and b==2 and c!=2) or (b==2 and c==2 and a!=2) or (c==2 and a==2 and b!=2):
    print(True)
else:
    print(False)