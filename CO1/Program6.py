class Complex:
    def __init__(self,real,img):
     self.real = real
     self.img = img
    def __add__(self,other):
       realpart = self.real + other.real
       imgpart = self.img + other.img
       print("Sum = ",realpart,"+i",imgpart)
    def __sub__(self,other):
       realpart = self.real - other.real
       imgpart = self.img - other.img
       print("Difference =",realpart, "+i",imgpart)
    def __mul__(self,other):
       realpart = self.real*other.real - self.img*other.img
       imgpart = self.real*other.real - self.img*other.img
       print("product =",realpart,"+i",imgpart)

r1 = int(input("Enter the real part of first number"))
i1 = int(input("Enter the imaginary part of first number"))
r2 = int(input("Enter the real part of second number"))
i2 = int(input("Enter the imaginary part of second number"))
c1 =  Complex(r1,i1)
c2 =  Complex(r2,i2)
print("Addition of 2 complex number")
c1 + c2
print("Subracting complex numbers ")
c1 - c2
print("Mutiplication of 2 complex numbers")
c1 * c2