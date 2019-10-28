class Matrix():
    def __init__(self,l):
        self.l = l

    def Arr(self):
        import random
        arr = [[random.random()*100 for  i in range( 0, self.l )] for j in range ( 0, self.l )]
        return arr

class Solution(Matrix):
    def __init__(self,l):
        super().__init__(l)






    def ex_432(self):
        import math
        M = Matrix
        arr = M.Arr()
        n=int(input())
        a = 0
        b = 0
        if n == 1:
            for i in range (0,self.l):
                for j in range (0,self.l-1-i):
                    if j > i:
                        if ( i + j ) % 2 != 0:
                            a += self.arr[i][j]**2
                            b += 1
                            sum = math.sqrt( a/b )
        elif n == 2:
            for i in range (self.l):
                for j in range (self.l):
                    if i + j == self.l-1:
                        if ( i + j ) % 2 != 0:
                            a += self.arr[i][j]**2
                            b += 1
                            sum = math.sqrt( a/b )

        return sum


    def ex_435(self):
        M = Matrix
        arr = M.Arr()
        sum = 0
        for i in range (0,self.l-1):
            for j in range(0,self.l-1-i):
                if j > i :
                    if (self.arr[i][j]//1)%5 ==0:
                        sum += 1
        return sum

    def ex_436(self):
        M = Matrix
        arr = M.Arr()
        a = int(input())
        b = int(input())
        x = 0
        y = 0
        for i in range (1,self.l):
            for j in range (0,i):
                if j < i:
                    if self.arr[i][j] > a and self.arr[i][j] < b:
                        x += self.arr[i][j]
                        y += 1
                        sum = x / y
        return sum


    def ex_439(self):
        M = Matrix
        arr = M.Arr()
        sum = 1
        for i in range (0,self.l-1):
            for j in range (i+1,self.l):
                if ( i + j ) % 2 != 0:
                    sum *= self.arr
        return sum


    def ex_440(self):
        M = Matrix
        arr = M.Arr()
        sum = 0
        for i in range (0,self.l-1):
            for j in range (i+1,self.l):
                if ( i + j ) % 2 == 0:
                    sum += self.arr[i][j]
        return sum


    def ex_442(self):
        M = Matrix
        arr = M.Arr()
        a = 0
        b = 0
        for i in range (0,self.l-1):
            for j in range (0, self.l-1-i):
                if self.arr[i][j] < 0:
                    a +=self.arr[i][j]
                    b += 1
                    sum =a / b
        return sum


    def ex_445(self):
        M = Matrix
        arr = M.Arr()
        k =int(input())
        a = 0
        b = 0
        for i in range (1,self.l):
            for j in range (0,i):
                if j < i:
                    if self.arr[i][j]<0:
                        if  -self.arr[i][j] > k:
                            a += 1
                    elif self.arr > k:
                        b += 1
        sum = a+b
        return sum

    def ex_447(self):
        M = Matrix
        arr = M.Arr()
        a =int(input("a = "))
        sum = 1
        print("ojandak ankyunagcic nerqev muqagrel 1 kam 2` ojandak ankyunagci var hashvelu hamar")
        n = int(input())
        if n == 1:
            for i in range  (1,self.l):
                for j in range (self.l-i,self.l):
                    if j < i:
                        if arr[i][j] < a:
                            sum *=arr[i][j]
            return sum
        elif n == 2:
            for i in range  (self.l):
                for j in range (self.l):
                    if i +j  == self.l-1:
                        if arr[i][j] < a:
                            sum *=arr[i][j]


        return sum

    
    def ex_449(self):
        M = Matrix
        arr = M.Arr()
        sum = 0
        for i in range (1,self.l):
            for j in range(0,self.l - 1 -i):
                if j < i:
                    if (arr[i][j]//1) % 4 == 0 :
                        sum += arr[i][j]
        return sum


