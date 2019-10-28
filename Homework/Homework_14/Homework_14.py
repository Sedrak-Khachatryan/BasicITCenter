class Vector:
    def __init__(self,n):
        self.n = n
    def Arr(self):
        import random
        arr = [random.randint(-100,100) for i in range (0,self.n)]
        return arr



class Solution:
    def __init__(self):
        self.arr = Vector(10).Arr()
    def ex_281(self):
        res = list(filter(lambda a: a>0,self.arr))
        return res
    def ex_282(self):
        arr_1 = list(filter(lambda a: a > 0, self.arr))
        arr_2 = list(filter(lambda a: a<0 ,self.arr))
        res = arr_1 + (arr_2)
        return res

    def ex_283(self):
        res = list(filter(lambda a: a%2!=0,self.arr))
        return res

    def ex_284(self):
        a = int(input())
        b = int(input())
        res = list(filter(lambda x: x>=a and x<=b,self.arr))
        return res

    def ex_285(self):
        p = int(input())
        res = list(filter(lambda a: a%p ==0,self.arr))
        return res

    def ex_286(self):
        res = list(filter(lambda a: a%2 == 0,self.arr))
        return res

    def ex_290(self):
        res = list(filter(lambda a: a%6 == 1),self.arr)
        return res




