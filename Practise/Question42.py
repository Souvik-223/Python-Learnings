#Write a program to print a copy of the text fie 
with open('Practise/log.txt','r') as f:
    x=f.read()

z =open('Practise/copy.txt','w')
z.write(x)
z.close()