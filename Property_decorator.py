class Employee:
    company = "Bharat gas"
    salary = 5600
    salarybonus = 500
    
    @property   # This are also called getter methods this are used to take values from the 
    def totalsalary(self):
        return self.salary + self.salarybonus
    
    @salary.setter
    def totalsalary(self,val):
        self.salarybonus = val - self.salary
    
e = Employee()
print(e.totalsalary)
r.totalsalary = 8000