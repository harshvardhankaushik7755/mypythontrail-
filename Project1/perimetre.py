import math

def perimetreOfSquare(side):
    pofasquare = 4 * side
    print("Perimetre: ", pofasquare, "units")
    
def perimetreOfRectangle(length, width):
    pofarect = (length + width)*2
    print("Perimetre: ", pofarect, "units")
    
def perimetreOfTriangle(length, width, hypotenuse):
    perimetre = length+width+hypotenuse
    print("Perimetre: ", perimetre, "units")
    
def perimetreOfCircle(radius):
    perimetre = 2*math.pi*radius
    print("Perimetre: ", perimetre, "units")
    
    
if __name__ == "__main__":
    userinput = None
    while userinput != "exit":
        print("If your operation requires 1 parametre write O, if 2 press T, if multiple press M")
        userinput = input()
        if userinput == "T":
            print("Choose operations in pofrectangle")
            userinput = input()
            if  userinput == "pofrectangle":
                print("Enter first no. ")
                userinputasnum1 = input()
                print("Enter second no. ")
                userinputasnum2 = input()
                userinputasnum1 = int(userinputasnum1)
                userinputasnum2 = int(userinputasnum2)
            if userinput == "pofrectangle":
                perimetreOfRectangle(userinputasnum1, userinputasnum2)
                    
        elif userinput == "M":
            print("Choose operations in poftriangle")
            userinput = input()
            if  userinput == "poftriangle":
                print("Enter first no. ")
                userinputasnum1 = input()
                print("Enter second no. ")
                userinputasnum2 = input()
                print("Enter third no.")
                userinputasnum3 = input()
                userinputasnum1 = int(userinputasnum1)
                userinputasnum2 = int(userinputasnum2)
                userinputasnum3 = int(userinputasnum3)
            if userinput == "poftriangle":
                    perimetreOfTriangle(userinputasnum1, userinputasnum2, userinputasnum3)
                    
        elif userinput == "O":
            print("Choose operations in aofsquare, aofcircle")
            userinput = input()
            if  userinput == "pofsquare" or userinput == "pofcircle":
                print("Enter first no. ")
                userinputasnum1 = input()
                userinputasnum1 = int(userinputasnum1)
                if userinput == "pofcircle":
                    perimetreOfCircle(userinputasnum1)
                if userinput == "pofsquare":
                    perimetreOfCircle(userinputasnum1)
                    
        elif userinput != "exit":
            print("Whatever you have written is not valid")
            
        else:
            print("THANKYOU!!")