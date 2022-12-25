# Write a class vector representing a vector of n dimension. overloaded the + and * operator which calculates the sum and the dot product of them.
class vector:
    def __init__(self,vec):
        self.vec=vec
        
    def __str__(self):
        str=''
        index=0
        for i in self.vec:
            str+= f"{i}a{index} +"
            index+=1
        return str[:-1]
        
    def __add__(self,vec2):
        add=[]
        for i in range(len(self.vec)):
           add.append(self.vec[i]+vec2.vec[i])
        return vector(add)
    
    def __mul__(self,vec2):
        mul=0
        for i in range(len(self.vec)):
           mul+=self.vec[i]*vec2.vec[i]
        return mul
    def __len__(self):
        self.len=len(self.vec)  
        return self.len
    
v1=vector([1,4,6])
v2=vector([4,3,5])
print(v1)
print(v1+v2)
print(v1*v2)
print(len(v1))
print(len(v2))