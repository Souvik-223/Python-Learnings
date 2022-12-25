#Check if a text fiel contains the bad words or not and if it conatins then replace those words with ######
words=["donkey","idiot","stupid"]
f=open('Practise/bad.txt','r')
content = f.read()

for i in words:
    if i in  content:
        content=content.replace(i, "####")
               
with open ('Practise/bad.txt','w') as f:
    f.write(content)