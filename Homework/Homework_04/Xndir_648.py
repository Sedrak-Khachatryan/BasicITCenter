n=input("")
a=n[n.find("x")+1  : ]
b=0
for i in a:
    if i =="0":
        b=b+1
print (b)