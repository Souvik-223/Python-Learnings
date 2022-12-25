#Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder. 
n=int(input("Enter the number you want the multiplication table of: "))
f=open("multiplication_table.txt","a")
    
for i in range (1,11):
    f.write(f"{n} x {i} = {n*i}\n")
f.close()