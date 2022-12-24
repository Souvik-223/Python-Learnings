#Write a program to find whether a given number is prime or not 
i = int(input("Enter a number: "))
for j in range(2,(i//2)+1):
    if(i%j == 0):
        print("The number is not prime")
        break
else:
    print("The number is prime")