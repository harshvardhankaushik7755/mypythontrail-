import random
random.randint(1,100)
jackpot = random.randint(1,100)
guess = int(input("guess the no. which I am thinking 5 billion dollars on the line "))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("guess higher ")
    else:
        print("guess lower ")
    guess = int(input("guess the no. which I am thinking 5 billion dollars on the line "))
    counter+=1
    print("you took ",counter,"attempts")
print("correct answer")