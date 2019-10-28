class Fraction_X ():
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    def New (self):
        from fractions import Fraction
        New_Fracton =Fraction( self.numerator/self.denominator)
        return New_Fracton

    def __eq__ (self,other):
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __gt__ (self,other):
        return self.numerator / self.denominator > other.numerator / other.denominator

    def __lt__ (self,other):
        return self.numerator / self.denominator < other.numerator / other.denominator

    def  __ne__ (self,other):
        return self.numerator/self.denominator != other.numerator / other.denominator

    def __add__(self, other):
        from fractions import Fraction
        sum = Fraction( (self.numerator * other.denominator + other.numerator * self.denominator),(self.numerator +other.numerator))
        return sum
    def __sub__ (self,other):
        from fractions import Fraction
        sum = Fraction((self.numerator * other.denominator - other.numerator * self.denominator) ,(self.denominator +other.numerator))
        return sum

    def __mul__ (self,other):
        from fractions import Fraction
        sum = Fraction((self.numerator * other.numerator) , (self.denominator * other.denominator))
        return sum

    def __truediv__(self,other):
        from fractions import Fraction
        sum = Fraction((self.numerator * other.denominator) , (self.denominator * other.numerator))
        return sum

a =Fraction_X(3,4)
b =Fraction_X(5,2)

print("a + b =",a+b)
print("a - b =",a-b)
print("a * b =",a*b)
print("a * b =",a/b)

