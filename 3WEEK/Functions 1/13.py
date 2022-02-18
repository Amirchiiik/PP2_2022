import imp


import random
name=input("Hello! What is your name?\n")
print("Well, "+name+", I am thinking of a number between 1 and 20")
trg=random.randint(1,21)
gs=int(input("Take a guess.\n"))
cnt=0
while(trg!=gs):
    if gs<trg:
        cnt+=1
        print("Your guess is too low.")
        gs=int(input("Take a guess.\n"))
    else:
        cnt+=1
        print("Your guess is too high.")
        gs=int(input("Take a guess.\n"))
else:
    print("Good job, "+name +f"! You guessed my number in {cnt} guesses!")


