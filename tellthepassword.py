USERINPUT = input("WRITE PASSWORD. If exit write 'exit'.")

if __name__ == '__main__':

    if USERINPUT!="exit":
        
        if USERINPUT == "PASSWORD":
            print("TRY AGAIN")
            OTHERINUT = input()
            if OTHERINUT == "AGAIN":
                print("You passed the password congrats!!")
        else:
            print("you failed.have another try")
            
    else:
        print("Thank you.")