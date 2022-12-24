class a:
    def __init__(self):
        print("This is __init__ of class a")

class b(a):
    def __init__(self):
        super().__init__()
        print("This is __init__ of class b")
        
        
class c(b):
    def __init__(self):
        super().__init__()
        print("This is __init__ of class c")
        
cat=c()
        
        