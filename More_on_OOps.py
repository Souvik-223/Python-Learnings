#Inheritance
class a:   #Parent class
    def greet(self):
        print("Good morning")

class b(a):   # Derived class
    def hello(self):
        print("Hello")
        
ander=a()
harry=b()

ander.greet()   #Object of parent class calls method of parent class
harry.greet()   #Object of child class calls method of child class




#Multiple inheritence 

class Employee:
    company="Google"
    salary=10000
    
class Freelancer:
    company="Personal"
    level=0 
    
    def upgrade(self):
        self.level = self.level+1
        
class person(Employee,Freelancer):
    name ="Harry"
    
harry = person()
harry.upgrade()
print(harry.level)
print(harry.company)   #This will print google as it is called first in the person class