import random
def computer():
    n=random.randint(1,3)
    return n

def check(x,n):
    if(x==n):
        print("Player and computer both choose the same-")
        print("Draw")
    elif(x==1 and n==2):
        print("Player Choose Snake and computer choose Water-")
        print("Player wins")
    elif(x==1 and n ==3):
        print("Player Choose Snake and computer choose Gun-")
        print("Computer wins")
        
    elif(x==2 and n ==1):
        print("Player Choose water and computer choose Snake-")
        print("Computer wins")
    elif(x==2 and n ==3):
        print("Player Choose water and computer choose Gun-")
        print("Player wins")
        
    elif(x==3 and n ==1):
        print("Player Choose Gun and computer choose Snake-")
        print("Player wins")
    elif(x==3 and n ==2):
        print("Player Choose Gun and computer choose Water-")
        print("Computer wins")
    
    
    
print("WELCOME TO SNAKE, WATER AND GUN GAME:-")
print("Choose from the following options below:-")
print("Press 1 for Snake")
print("Press 2 for Water")
print("Press 3 for Gun")
x=int(input("Enter Your choice: "))
n=computer()
check(x,n)

