f=open('sample.txt','r')
data = f.read()   #Reads the entire text present in the text file 
data2 = f.readline()  #Reads only one line from the file
print(data)
print(data2)
f.close()

# Writing to the file - This will replace any text present in the file an dwil write the added data into the file"
# If there is no file present in the disk with that file name then the write operation will create the file first and then will start writing in the file 
f=open('Another.txt','w')
f.write("Please write this to the file")
f.close()

# Appending in the text file - This add text at the end of the file 
f=open('Another.txt','a')
f.write("I am appending")

# Using the with statement - This allows the file to be open but it is not necessay to close the file 
with open('Another.txt','w') as f:
    f.write("This is the with statement")