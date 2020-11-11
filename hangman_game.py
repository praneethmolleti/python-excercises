import time
name=input("Enter your name:")
print("hello",name,"time to play Hangman!")
time.sleep(1)
print("start guessing")
time.sleep(0.5)
word="secret"
guesses=""
turns=10
while turns>0:
    failed=0
    for i in word:
        if i in guesses:
            print(i)
        else:
            print("_")
            failed+=1
    if failed==0:
        print("You Won")
        break
    guess=input("guess the character:")
    guesses+=guess
    if guess not in word:
        turns-=1
        print("Wrong")
        print("You have",turns,"more guesses")
        if turns==0:
            print("You loose")

