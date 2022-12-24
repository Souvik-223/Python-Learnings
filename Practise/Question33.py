#Write a program to print multiplication table of n in reverse order
n = int(input("Enter the number: "))
for i in range (10,1,-1):
    print(f"{n} x {i} = {n*i}")