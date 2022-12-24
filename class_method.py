class Employee:
    company = "Google"
    salary = 10000
    
    @classmethod   #This will allow the user to change any class attribute by user input  
    def changesalary(cls,sal):
        cls.salary = sal


    #The below function also wil do the same thing as class method
    # def changesalary(self,sal):
    #     self.__class__.salary = sal
        

e = Employee()
print(e.salary)
e.changesalary(5000)
print(e.salary)