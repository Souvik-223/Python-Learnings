#Write a program to print thr factorial of a given number using for loop
a=int(input("Enter the number to get its factorial: "))
num=1
for i in range(1,a+1):
    if(a==0):
        print(1)
    num = num*i  
print(num)