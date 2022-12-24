#Write a python function to remove a given word from a string and strip it at the same time.
def rmov(word,l):
    newstr = l.replace(word,"")  #It replaces the word with a blank so it removes the word from the string
    return newstr.strip()  #Strip() is used to remove all the white space from both sides of a sentence 

l="  Hellow this is harry   "
x=rmov("Hellow",l)
print(x)