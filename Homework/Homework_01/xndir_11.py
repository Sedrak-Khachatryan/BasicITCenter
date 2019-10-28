import math

a = float(input())
b = float(input())
x = float(input())
c = math.pow(a, 2) + math.pow(b, 2)
if c > 5:
    y = 3 * math.exp(a - x) + math.log(3, (math.pow(a, 2) + math.pow(b, 2) + 5))
    print(y)

if c < 1:
    y = math.pow(math.tan(a + b), 4)
    print(y)

else:
    print(-3)