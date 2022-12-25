#Write a class complex to represent complex numbers, along with overloaded operators  + and * which adds and multiplies them 
class complex:
    def __init__(self,integer,imaginary):
        self.integer = integer
        self.imaginary=imaginary  
    def __add__ (self,num2):
        i=self.integer + num2.integer
        img=self.imaginary + num2.imaginary
        return f"{i}+{img}i"
        
    def __mul__(self,num2):
        i= self.integer * num2.integer
        i2= self.integer * num2.imaginary
        i3= self.imaginary * num2.integer
        i4= self.imaginary * num2.imaginary
        integer = i-i4
        img=i2+i3
        return f"{integer}+{img}i"

c=complex(5,4)
c2=complex(6, 9)
print(c+c2)
print(c*c2)