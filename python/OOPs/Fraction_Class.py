class Fraction:
    def __init__(self,x,y):
        self.num = x
        self.den = y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(self,other):
        new_num = self.num*other.den + self.den*other.num
        new_den = self.den * other.den
        return Fraction(new_num,new_den)
    
    def __sub__(self,other):
        new_num = self.num*other.den - self.den*other.num
        new_den = self.den * other.den
        return Fraction(new_num,new_den)    
    
    def __mul__(self,other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num,new_den)
    
    def __truediv__(self,other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num,new_den)
    

f1 = Fraction(1,2)
f2 = Fraction(3,4)

print("f1: ",f1)
print("f2: ",f2)

print("f1 + f2: ",f1+f2)
print("f1 - f2: ",f1-f2)    
print("f1 * f2: ",f1*f2)
print("f1 / f2: ",f1/f2)