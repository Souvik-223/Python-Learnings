# Write a function using functions to find the greatest of three numbers
def max(a, b, c):
    m = a
    for i in range(3):
        if(a > m):
            m = a
        elif(b > m):
            m = b
        elif(c > m):
            m = c
    print(m)


max(3, 5, 8)
