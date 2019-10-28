import math
a=int(input())
b=int(input())
c=int(input())
if a==math.sqrt(b*c) or b==math.sqrt(a*c) or c==math.sqrt(a*b):
    print(True)
else:
    print(False)