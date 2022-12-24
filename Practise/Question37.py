#Write a pyhton function to print the multiplication table of the given number 
def mul(n):
    for i in range (10):
        print(f"{n} x {i} = {n*i}")

n=int(input("Enter the number to get the multiplication table of: "))
mul(n)