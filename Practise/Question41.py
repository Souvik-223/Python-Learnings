# Write a program to check if 'python' is present in the log.txt amd in which line number
i = 0
content=True
with open('Practise/log.txt', 'r') as f:
    while content:
        content = f.readline()

        if 'python' in content:
            print("Yes python is present in the file")
        i += 1

print("The line number is ", i-1)
