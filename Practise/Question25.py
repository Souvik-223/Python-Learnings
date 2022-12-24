#Check for specific spam comments in the text entered by the user
text= input ("Enter the text of your choice ")
spam = False

if("Make a lot of money" in text):
    spam=True
elif("Buy now" in text):
    spam=True
elif("Click this" in text):
    spam=True
elif("Subscribe this" in text):
    spam=True
else:
    spam=False
    
if(spam):
    print("This text file contains spam")
else:
    print("It dosen't contain spam")

 