#Replace the double spaces with single spaces in question 8
a = '''Dear  <|Name|> 
you are selected! 
Date: <|Date|>
'''
a=a.replace("  "," ")
print(a)