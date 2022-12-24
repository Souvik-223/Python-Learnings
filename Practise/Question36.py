#Write a python function to print first n lines of the following pattern:- 
def pattern(n):
    if(n==0):
        return
    for i in range (n):
        print("*",end="")
    print()
    pattern(n-1)
    
n =int(input("Enter the numbr of lines you want: "))
pattern(n)