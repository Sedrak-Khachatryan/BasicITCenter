a=[12,50,-60,3,-3,9,-1,8,10,20,30,-54]
b=1
t=22
for i in a:
    if i<t and -i>-t:
        b=b*i
print(b)