

def getAnglename(angle):
    if angle <90:
        print("Acute angle: ", angle)
    elif angle == 180:
        print("Straight angle:", angle)
    elif angle == 360:
        print("Complete angle: ", angle)
    elif angle == 90:
        print("Right angle: ", angle)
    elif angle> 90:
        print("Obtuse angle: ", angle)
    else:
        pass
if __name__ == "__main__":
    userinput = None
    while userinput!="exit":
        print("Do you want to know types of angles if yes,  press y, else write exit")
        userinput = input()
        if userinput == "y":
            print("Write your angles measurement")
            userinput = input()
            userinput = float(userinput)
            getAnglename(userinput)
        elif userinput!= "exit":
            print("Whatever you have written is wrong")
        else:
            print("Thank you !!!")