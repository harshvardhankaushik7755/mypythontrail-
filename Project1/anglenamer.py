

def acuteAngle(angle):
    print("Acute angle: ", angle)
    
def obtuseAngle(angle):
    print("Obtuse angle: ", angle)
    
def righttAngle(angle):
    print("right angle: ", angle)
    
def completeAngle(angle):
    print("Complete angle: ", angle)
    
    
if __name__ == "__main__":
    userinput = None
    while userinput!="exit":
        print("Do you want to know types of angles press y, else write exit")
        userinput = input()
        if userinput == "y":
            print("Write your angles measurement")
            userinput = input()
            userinput = int(userinput)
            if userinput <90:
                acuteAngle(userinput)
            elif userinput == 360:
                completeAngle(userinput)
            elif userinput>360:
                print("Too high press between 1 and 360")
            elif userinput>90:
                obtuseAngle(userinput)
            elif userinput == 90:
                righttAngle(userinput)
                
        elif userinput == "exit":
            print("Thankyou!!!!!!!")
            
        elif userinput!= "exit":
            print("Whatever you have written is incorrect")