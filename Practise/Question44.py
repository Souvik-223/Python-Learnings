#Write a class calculator capable of finding the square , cube and squareroot of a number 
import math
class calculator:
    def squareroot(self,n):
        print("The squareroot of the number is ")
        print(math.sqrt(self.n))
        
    def square(self,n):
        print("The square of the number is ")
        print((self.n)*(self.n))
        
    def cube(self,n):
        print("The cube of the number is ")
        print((self.n)*(self.n)*(self.n))
        
cal=calculator()
n=int(input("Enter the number you want: "))
cal.n=n
cal.square(n)
cal.squareroot(n)
cal.cube(n)