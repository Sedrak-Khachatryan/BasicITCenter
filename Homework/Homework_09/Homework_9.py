#437,449 ev 450-@ chem grel randomin float arjeq tal chkaroxanalu,internet-i bacakayutyan ev randomi dasin chgalu patcharov :)


#Trvac en n amboxj tiv@ ev n*n chapi matric, kazmel cragir ,vor@ khashvi ev ktpi matrici`

#payman,n -i arjeq@ chem karoxacel jisht dzevov mtcnel function-i mej,vor functian 2 arjeq veradardzni mek@ x-i,myus@ n-i hamar
n=int(input("mutqagreq n-i arjeq@"))
def matric(pahanj):
    import random
    x=[[random.randint(-100,100) for i in range (n)] for j in range(n)]
    return x



#ex_434 Ojandak ankyunagcic nerqev kam nra vra gtnvox ayn tarreri gumar@,voronc bacardzak arjeq@ patkanum e [5,4:15,3] mijakayqin
def ex_434(function_1):
    import math
    print("Ojandak ankyunagciv verev hashvelu hamar mutqagrel - 1 \nOjandak ankyunagci vra hashvelu hamar - 2")
    m=int(input())
    a=0
    x=function_call(matric)
    if m==1:
        for i in range(1,n):
            for j in range(n-i,n):
                if j<i:
                    if math.fabs(x[i][j])>5.4 and math.fabs(x[i][j])<15.3:
                        a=a+x[i][j]

    elif m==2:
        for i in range (n):
            for j in range(n):
                if i+j==n-1:
                    if math.fabs(x[i][j])>5.4 and math.fabs(x[i][j])<15.3:
                        a=a+x[i][j]
    return print("ex_434 = "+str(a))

def function_call(function):
    return function(ex_434)
function_call(ex_434)
print(function_call(matric))




#ex_436 Glxavor ankyunagcic nerqev gtnvox ayn tarreri mijin tvabanakan@,voronc arjeqner@ patkanum en trvac [a:b] mijakayqin
def ex_436(function_2):
    a=int(input("mutqagrel a-i arjeq@:"))
    b=int(input("mutqagrel b-i arjeq@:"))
    c=0
    d=0
    x=function_call(matric)
    for i in range(1,n):
        for j in range(0,i):
            if j<i:
                if x[i][j]>a and x[i][j]<b:
                    c+=x[i][j]
                    d+=1
    return print("ex_436 = "+str(c/d))

def function_call(function):
    return function(ex_436)
function_call(ex_436)
print(function_call(matric))




#ex_438 Glxavor ankyunagcic nerqev gtnvox ayn drakan tarreri qanak@,voronq gtnvum en zuyg hamarov syunerum
def ex_438(function_3):
    a=0
    x=function_call(matric)
    for i in range (1,n):
        for j in range(0,i):
            if j%2==0:
                if x[i][j]>0:
                    a+=1
    return print("ex_438 = "+str(a))

def function_call(function):
    return function(ex_438)
function_call(ex_438)
print(function_call(matric))




#ex_439 Glxavor ankyunagcic verev gtnvox ayn tarreri artadryal@,voronc indexneri gumar@ kent e.
def ex_439(function_4):
    a=1
    x=function_call(matric)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if j>i:
               if  (i+j)%2!=0:
                   a=a*x[i][j]
    return print("ex_439 = "+str(a))

def function_call(function):
    return function(ex_439)
function_call(ex_439)
print(function_call(matric))




#ex_440 Glxavor ankyunagcic vervev gtnvox ayn tarreri qanak@, voronc indexneri gumar@ zuyg e.
def ex_440(function_5):
    a=0
    x=function_call(matric)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if j>i:
                if (i+j)%2==0:
                    a+=1
    return print("ex_440 = "+str(a))

def function_call(function):
    return function(ex_440)
function_call(ex_440)
print(function_call(matric))





#ex_441 Glxavor ankyunagcic verev drakan tarreri mijin qarakusayin@
def ex_441(function_6):
    import math
    a=0
    b=0
    x=function_call(matric)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if j>i:
                if x[i][j]>0:
                    a=a+x[i][j]**2
                    b+=1
    return print("ex_441 = "+str(math.sqrt(a/b)))

def function_call(function):
    return function(ex_441)
function_call(ex_441)
print(function_call(matric))




#ex_442 Ojandak ankyunagcic verv gtnvox bacasakan tarreri mijin tvabanakan@
def ex_442(function_7):
    a=0
    b=0
    x=function_call(matric)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if j>i:
                if x[i][j]<0:
                    a+=x[i][j]
                    b+=1
    return print("ex_442 = "+str(a/b))


def function_call(function):
    return function(ex_442)
function_call(ex_442)
print(function_call(matric))





#ex_445 Glxavor ankyunagcic nerqev gtvox ayn tarreri qanak@,voronq bacardzak arjeqov mec en trvac k tvic.
def ex_445(function_8):
    x=function_call(matric)
    k=int(input("mutqagrel k-i arjeq@:"))
    a=0
    b=0
    for i in range(1,n):
        for j in range(0,i):
            if x[i][j]>k:
                a+=1
            elif    x[i][j] < 0:
                x[i][j] = -x[i][j]
                if x[i][j] > k:
                    b+= 1
    return print("ex_445 = "+str(a+b))

def function_call(function):
    return function(ex_445)
function_call(ex_445)
print(function_call(matric))




#ex_447 Ojandak ankyunagcic nerqev kam nra vra gtnvox ayn tarreri artadryal@, voronq poqr en trvac a tvic.
def ex_447(function_9):
    x=function_call(matric)
    m=int(input("Ojandak ankyunagcic nerqev hashvelu hamar mutqagrel - 1\nOjandak ankyunagci vra hashvelu hamar - 2"))
    a=int(input("Mutqagrel a-i arjeq@:"))
    b=1
    if m==1:
        for i in range(1,n):
            for j in range(n-i,n):
                if j>i:
                    if x[i][j]<a:
                        b=b*x[i][j]
        print("ex_447 = "+str(b))
    elif m==2:
        for i in range(n):
            for j in range(n):
                if i+j == n-1:
                    if x[i][j]<a:
                        b=b*x[i][j]
        print("ex_447 = "+str(b))

def function_call(function):
    return function(ex_447)
function_call(ex_447)
print(function_call(matric))

