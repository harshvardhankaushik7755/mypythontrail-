def getgender(gen):
    print("WELCOME TO GENDERAKINATOR")
    gen = input()
    if (gen =='thankyou'):
        print("Do you have long hairs:")
    elif (gen=='yes'):
        print("Do you play/like with dolls?")
    elif (gen =='no'):
        print("Do you play/like with dolls?")
    elif (gen =='no'):
        print("Your gender is male")
    elif (gen=='yes'):          
        print("Your gender is female")
    
    if __name__ == '__main__':
        getgender(gen)
        print("WELCOME TO GENDERAKINATOR")
    while (gen!='exit'):
            gen = input()
            if (gen!='exit'):
                print("The value you have given is not the correct option")
            else:             
                print("THANK YOU FOR USING GENDER AKINATOR")
                break             