import random
def check(comp, user):
    comp = random.randint(0, 1, 2)
    user = int(input("0 for rock 1 for paper 2 for scissors"))
    if(comp == 1 and user == 2):
        print("computer has won!")
    elif(comp == 2 and user == 1):
        print("You have won!")
    elif(comp == 0 and user == 2):
        print("computer has won!")
    elif(comp == 2 and user == 0):
        print("you have won!")
    elif(comp == 1 and user == 2):
        print("computer has won!")
    elif(comp == 2 and user == 1):
        print("computer has won!")
    elif(comp == 2 and user == 2):
        print("TIE!")
    elif(comp == 1 and user == 1):
        print("TIE!")
    elif(comp == 0 and user == 0):
        print("TIE!")
    elif(user == 'exit'):
        print("THANK YOU FOR USING ROCK PAPER SCISSORS!")

if __name__=='main':
    check()
        