import math

def cubeVolumeGiver(side):
    volume = side*6**2
    print("Volume: ", volume)
    
def cuboidVolumeGiver(length, width, height):
    volume = length*width*height
    print("Volume: ", volume)
    
def sphereVolumeGiver(radius):
    volume = 4/3*math.pi*radius**3
    print("Volume: ", volume)
    
    
if __name__ == "__main__":
    userinput = None
    while userinput != "exit":
        print("If your operation requires 1 parametre write O, if multiple press M")
        userinput = input()
        if userinput == "O":
            print("Choose operations in vofcube, vofsphere")
            userinput = input()
            if  userinput == "vofcube" or userinput == "vofsphere":
                print("Enter first no. ")
                userinputasnum1 = input()
                userinputasnum1 = int(userinputasnum1)
                if userinput == "vofsphere":
                    sphereVolumeGiver(userinputasnum1)
                if userinput == "vofcube":
                    cubeVolumeGiver(userinputasnum1)

        if userinput == "M":
            print("Choose operations in vofcuboid")
            userinput = input()
            if  userinput == "vofcuboid":
                print("Enter first no. ")
                userinputasnum1 = input()
                print("Enter second no.")
                userinputasnum2 = input()
                print("Third no. ")
                userinputasnum3 = input()
                userinputasnum1 = int(userinputasnum1)
                userinputasnum2 = int(userinputasnum2)
                userinputasnum3 = int(userinputasnum3)
                if userinput == "vofcuboid":
                    cuboidVolumeGiver(userinputasnum1)
                    
        elif userinput!="exit":
            print("Whatever you have written is invalid")
            
        else:
            print("Thank You")
    