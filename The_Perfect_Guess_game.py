import random
rand = random.randint(1, 100)
# print(rand)
userguess=None
guesses =0 
while(userguess != rand):
    userguess = int(input("Enter the number of your choice: "))
    if(userguess == rand):
        print("You guessed it right the number is ",userguess)
        guesses+=1
    else:
        print("You guessed it wrong! - Try again")
        guesses+=1
        if(userguess<rand):
            print("You should guess something bigger.")
        else:
            print("You should guess something smaller.")
print()
print("The number of guesses you took was ",guesses)


#This maintains a file of highscores and stores and shows some results- 
with open ("highscore.txt","r") as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("You have just broken the highscore!")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))