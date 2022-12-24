class Number:
    def __init__(self,num):
        self.num = num
    
    def __add__(self,n):    #This dunder method is used to provide add functionality in python. It recognises '+'
        print("Lets add")
        return self.num + n.num
    
    def __mul__(self,n2):  #This dunder method is used to provide multiply functionality in python. It recognises '*'
        print("Lets add")
        return self.num + n2.num
    
    #Other dunder methods 
    def __str__(self):      #This dunder methos is used to return for any call of str(obj).
        return f"Decimal number: {self.num}"
    
    def __len__(self):      #This dunder methos is used to return for any call of len(obj).
        return 1   #This says that the length for all the objects under Number class will be 1 by default. 
    

n1=Number(4)
n2=Number(6)
sum=n1+n2
mul=n1*n2
print(sum)
print(mul)

#Using other dunder method
n=Number(9)  
print(n)   #It calls str(obj) which then is provided under dunder method __str__ .
print(len(n))   #It calls len(obj) which then is provided under dunder method __len__ .