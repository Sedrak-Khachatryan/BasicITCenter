print ("x-in ev y-in tal tvayin arjeq")
import math
x=input()
y=input()
a=math.cos((math.pow(x,2)-y)/(math.pow(x,2)+math.pow(y,2)))/math.sin((math.pow(x,2)-y)/(math.pow(x,2)+math.pow(y,2)))+math.log(math.pow(x,2)+1)
print(a)