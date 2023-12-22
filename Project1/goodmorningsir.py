import random
def guess(z):
    random_num = random.randint(z)
    z = z>=100
    
    guess = int(input(print("Guess the no. I am thinking of (under 100)")))

    if guess == random_num:
        print(f"You are correct yhe no. is {random_num}")
        
    if guess >= random_num:
        print("Too low")
    
    if guess <= random_num:
        print("Too high")
        
        
if __name__ == '__main__':
    guess(z)