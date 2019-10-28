#Xndir_1
def Xndir_1(func_1):
    sum=0
    n=int(input())
    def rec_1(n,sum):
        if n==0:
            return
        sum +=n
        print(sum)
        rec_1(n-1,sum)
    rec_1(n,sum)


#Xndir_2
def Xndir_2(func_2):
    a=input("")
    def rec_2(a):
        b=len(a)
        if len(a)==0:
            return
        print(a[0])
        rec_2(a[1:])
    rec_2(a)

#Xndir_3
def Xndir_3(func_3):
    f=open("Xndir_3.txt","r")
    s=f.readlines()
    a=s[0].split(",")
    b=s[1].split(",")
    del a[-1]

    a = [int(i) for i in a]
    b = [int(i) for i in b]

    x=max(a)
    y=min(b)

    z=x*y


    f.close()
    return print(z)

#Xndir_4
def Xndir_4(func_4):
    f=open("Xndir_4.txt")
    s=f.readlines()
    a=s[0].split("a")
    b=s[1].split("z")
    c=s[2]
    z=0
    for i in c:
        if i =="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
            z+=1
    print(c)
    x=len(a)-1
    y=len(b)-1
    print("'a' tari qanak@ 1-in toxum >>>"+str(x),"\n'z' tari qanak@ 2-rd toxum >>>"+str(y),"\nTvanshaneri qanak@ 3-rd toxum >>>"+str(z))


    f.close()

#Xndir_5
def Xndir_5(func_5):
    import random
    n=5
    arr=[random.randint(-100,100) for i in range (n)]
    sum=0
    for i in arr:
        sum+=i
    f=open("Xndir_5.txt","w")

    f.write(str(sum))
    f.close()

#Xndir_6
def Xndir_6(func_6):
    f=open("Xndir_6.txt","r")
    s=f.readlines()
    a=0
    for i in s:
        if len(i)>10:
            a+=1
    print(a)

    f.close()

#Xndir_7
def Xndir_7(func_7):
    f=open("Xndir_7.txt","r")
    s=f.readline()
    a=s.split(",")
    a=[float(i) for i in a]
    x=0
    y=0
    for i in a:
        x+=i
        y+=1
        z=x/y
    print(z)

    f.close()

#Xndir__1_dec
def Dec_Xndir_1(dec_1):
    return dec_1(Xndir_1)
Dec_Xndir_1(Xndir_1)

#Xndir_2_dec
def Dec_Xndir_2(dec_2):
    return dec_2(Xndir_2)
Dec_Xndir_2(Xndir_2)

#Xndir_3_dec
def Dec_Xndir_3(dec_3):
    return dec_3(Xndir_3)
Dec_Xndir_3(Xndir_3)

#Xndir_4_dec
def Dec_Xndir_4(dec_4):
    return dec_4(Xndir_4)
Dec_Xndir_4(Xndir_4)

#Xndir_5_dec
def Dec_Xndir_5(dec_5):
    return dec_5(Xndir_5)
Dec_Xndir_5(Xndir_5)

#Xndir_6_dec
def Dec_Xndir_6(dec_6):
    return dec_6(Xndir_6)
Dec_Xndir_6(Xndir_6)

#Xndir_7_dec
def Dec_Xndir_7(dec_7):
    return dec_7(Xndir_7)
Dec_Xndir_7(Xndir_7)