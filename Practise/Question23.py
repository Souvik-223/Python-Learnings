#Write a program to find the greatest of four numbers entered by the user
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
d=int(input("Enter a number"))
x=0
if(a>b):
   x=a 
else:
    x=b
    
if(b>c):
    x=b
else:
    x=c

if(c>d):
    x=c
else:
    x=d

if(d>a):
    x=d
else:
    x=a
    
print(x)