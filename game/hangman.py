import random

name=input("Enter your name")

print("All the Best",name)

words=['apple','ball','cat','dog']

word=random.choice(words)

#print(word)
guesses=''
turns=3
while turns>0:
    fail=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("------")
            fail+=1
    if fail==0:
        print("You win the game")
        print("The Word is:",word)
        break

    guess=input("Guess the character:")
    guesses+=guess

    if guess not in word:
        turns-=1
        print('Your guess is wrong')
        print("you have",turns,"more guesses available")

    if turns==0:
        print("sorry",name,"you lost the secret word was",word)
