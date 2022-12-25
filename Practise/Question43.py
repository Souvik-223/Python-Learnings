#Write a program to check if two files are identical 
with open('Practise/log.txt','r') as f:
    x=f.read()
with open('Practise/copy.txt','r') as f:
    z=f.read()

if x==z :
    print("Both files are identical")
else:
    print("Files are not identical")