#Write a program to greet all the persons names stored in a list l1 and which starts with s 
l1=["Harry,","Soham","Sachin","Rahul"]

for i in l1:
    if (i.startswith('S')):
        print("Hello",i)
    else:
        continue
    