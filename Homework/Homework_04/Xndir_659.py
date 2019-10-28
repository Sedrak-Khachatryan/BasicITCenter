n=input("")
x=0
for i in n:
    if i == "x":
        for a in n:
            if a=="c":
                x=x+1
    elif i=="d":
        x=x+1

print(x)