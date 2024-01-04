import math

def perimetreOfCube(side):
    perimetre = 12*side
    print("Perimetre: ", perimetre)
    
def perimetreoOfCuboid(length, width, height):
    perimetre = 4*length*width*height
    print("Perimetre: ", perimetre)
    
def circumferenceOfSphere(radius):
    circumference = 2*math.pi*radius
    print("Circumference: ", circumference)
    
    
if __name__ == "__main__":
    userinput = None
    while userinput!="exit":
        print("If your operation requires single parametre press O, if multiple press M")
        userinput = input()
        if userinput == "O":
            print("Choose operations in pofcube, cofsphere")
            userinput = input()
            if userinput == "pofcube" or userinput == "cofsphere":
                print("Enter the no.")
                userinputasnum1 = input()
                if userinput == "pofcube":
                    perimetreOfCube(userinputasnum1)
                if userinput == "cofsphere":
                    circumferenceOfSphere(userinputasnum1)
                    
        elif userinput == "M":
            print("Choose operation pofcuboid")
            userinput = input()
            print(userinput)
            if userinput == "pofcuboid":
                print("Enter first no.")
                userinputasnum1 = input()
                print("Enter the second no.")
                userinputasnum2 = input()
                print("Enter the no.")
                userinputasnum3 = input()
                userinputasnum1 = int(userinputasnum1)
                userinputasnum2 = int(userinputasnum2)
                userinputasnum3 = int(userinputasnum3)
                perimetreoOfCuboid(userinputasnum1, userinputasnum2, userinputasnum3)
                    
        elif userinput != "exit":
            print("Whatever you have printed is wrong")
            
        else:
            print("THANKYOU!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
                

