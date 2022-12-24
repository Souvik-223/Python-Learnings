#Detect the double spaces within in question 7
a = '''Dear  <|Name|> 
you are selected! 
Date: <|Date|>
'''
x=a.find("  ")
print(x)