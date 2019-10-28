"""n=input("")
a=n[n.find("z") +1 : ]
b=a[a.find("z") +0 : ]

print(len(a)-len(b))"""
a="dasdasdzbbx1z002"
pos=-1
count=0
for i in range(len(a)):
   if  a[i]=='z':
       if pos!=-1:
           break
       pos=i
   if pos !=-1:
        count +=1
print (count)


for i in range(pos+q+1,len(a)):
