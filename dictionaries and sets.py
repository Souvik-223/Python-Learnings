# Dictionary
a={1:"Souvik" , 2:"Subhadip", 3:"Soutrik"}

print(a[3])
print(a.items())   #Returns a list of (key,value) tuples
print(a.keys())    #Returns the list of all the keys preset in the dictornaries
a.update({2:"Souvik"})      #Updates the variables in the provided key in the dictinoary  
print(a.get(3))   #Takes a key and returns the value in the dictionary 


# Sets in python

set = {1,2,3,4,4,5}  # Sets cannot contain duplicate value in python 
print(set)

set.add(45)
set.remove(4)
set.pop()
print(set.union({8,7,30}))
print(set.intersection({8,7,30}))
print(set)
set.clear()
