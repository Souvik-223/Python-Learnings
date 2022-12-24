class Employee:     #It is the instiation of a Class i.e Xreating a class  
    company = "Google"    # This is a class attribute
    salary = 60000
    def getsalary():   # It is a method defined within a class 
        print("60,000")
    
    def __init__(self,name,sal,age):  #It is a constructor that is used to declare objects with specified fields 
        print("This is the __init__ constructor")
        self.name=name
        self.sal=sal
        self.age=age
    
    def getdetails(self):
        print(f"The name is {self.name}")
        print(f"The salary is {self.sal}")
        print(f"The age is {self.age}")
        
    
class Life:
    def Eating(Self,Food):   # It is used to denote the class object inside a function through which all the attributes can be used with in a function.
        print(f"This {Self} is eating {Food}")
        
    @staticmethod
    def time():   # It is a static method so it wouldn't need a self refrence of object to run. 
        print("The time is 9am")
        
harry=Employee("Harry",100,23)    # This is the creation of an object from a class
# ravesh=Employee()
harry.salary = 45000  # This is an Instance attribute 

print(harry.salary)  # It will fetch the instance variable 
# print(ravesh.salary) # It will fetch the class variable as there is no instance variable present 
# print(ravesh.address) # It will try to fetch the class variable and since there is no class varible so it will throw an error to the compiler  

habib=Life()
habib.Eating("Mango")   # It is equivalent to  Life.Eating(habib)

habib.time()   #It wouldn't throw an error as the time is a static function and it can be declared without passing the object as self refrence to the function.


harry.getdetails()   #It is actually used to pass values in the constructor which will be used in a function to get the values 