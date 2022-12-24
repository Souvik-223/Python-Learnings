'''
pattern
***
* *
***
'''
n=3
for i in range (3):
    if(i==0):
        print("*" * (n)) 
    if(i != (0 or n-1)):
        print("*" * 1,end="")
        print(" " * (n-2),end="")
        print("*" * 1)
    else:
        print("*" * (n))  