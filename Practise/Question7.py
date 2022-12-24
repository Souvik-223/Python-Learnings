#Write a python program to fill the letter template given below with name and date 
a = '''Dear <|Name|> 
you are selected! 
Date: <|Date|>
'''
name = input("Enter your name ")
Date = input("Enter Date ")
a=a.replace("<|Name|>",name)
a=a.replace("<|Date|>",Date)
print(a)