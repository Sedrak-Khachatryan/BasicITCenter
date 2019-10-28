import math

x = 5
while x > 0:
    y = math.pow(x, 2) + 4 * math.pow(x, 8)
    print(y)
    x = x - 2

else:
    print(0)