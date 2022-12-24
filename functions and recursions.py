def func( a, b):
    sum= a+b
    return sum    


def func2(a,b):   #Function in recursion
    sum = a +b
    if (sum<=0):
        print (sum)
        return
    print(sum)
    func2(a-1,b-1)



a= 10
b= 8
c = func(a,b)
print(c)
func2(a,b)