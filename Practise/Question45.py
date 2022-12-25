#Create a class and check if changing instance varibale changes class variable and create a static method to greet the programmer
class major:
    a=45
    @classmethod
    def prt(cls):
        print(cls.a)
    
    @staticmethod
    def greet():
        print("Good morning")

m=major()
m.a=64
m.prt()
m.greet()
