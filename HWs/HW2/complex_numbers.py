import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, a):
        return Complex(self.real + a.real, self.imaginary + a.imaginary)
        
    def __sub__(self, a):
        return Complex(self.real - a.real, self.imaginary - a.imaginary)
                
    def __mul__(self, a):
         return Complex(self.real * a.real - self.imaginary * a.imaginary,
                        self.real * a.imaginary + self.imaginary * a.real)
        
    def __truediv__(self, a):
        return Complex((self.real * a.real + self.imaginary * a.imaginary) / (a.real ** 2 + a.imaginary ** 2),
                        (self.imaginary * a.real - self.real * a.imaginary) / (a.real ** 2 + a.imaginary ** 2))
        
    def mod(self):
        return Complex((self.real ** 2 + self.imaginary ** 2) ** 0.5, 0)
        
    def __str__(self):
        if self.imaginary == 0:
            result = f"{self.real:.2f}+0.00i"
        elif self.real == 0:
            if self.imaginary >= 0:
                result = f"0.00+{self.imaginary:.2f}i"
            else:
                result = f"0.00-{abs(self.imaginary):.2f}i"
        elif self.imaginary > 0:
            result = f"{self.real:.2f}+{self.imaginary:.2f}i"
        else:
            result = f"{self.real:.2f}-{abs(self.imaginary):.2f}i"
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
