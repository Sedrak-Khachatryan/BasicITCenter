import math
x = -5.4
while x <= 1.2:
    y = (math.cos(math.pow(x, 2)) * math.cos(math.pow(x, 2))) / (math.sin(math.pow(x, 2)) * math.sin(math.pow(x, 2)))
    print(y)
    print(x)
    x = x + 0.4
