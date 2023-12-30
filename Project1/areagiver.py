import math

def areaOfRectangle(length, breadth):
    area = length*breadth
    print("Area:", area, "units")

def areaOfSquare(side):
    area = side*side
    print("Area: ", area, "units")
    
def areaOfTriangle(height, base):
    area = 1/2 * base *height
    print("Area: ", area, "units")

def areaOfCircle(radius):
    area = math.pi * pow(radius)
    print("Area: ", area, "units")
    
def areaOfParallelogram(length, breadth):
    area = length*breadth
    print("Area:", area, "units") 
    
def areaOfRhombus(length, breadth):
    area = ((length*breadth)/2)
    print("Area: ", area , "units")
    
    
if __name__ == "__main__":
    userinput = None
    while userinput != "exit":
        print("If your operation requires 1 parametre write O, if multiple press M")
        userinput = input()
        if userinput == "M":
            print("Choose operations in aofrectangle, aofparallelogram, aoftriangle")
            userinput = input()
            if  userinput == "aofrectangle" or userinput == "aofparallelogram" or userinput == "aoftriangle":
                print("Enter first no. ")
                userinputasnum1 = input()
                print("Enter second no. ")
                userinputasnum2 = input()
                userinputasnum1 = int(userinputasnum1)
                userinputasnum2 = int(userinputasnum2)
                if userinput == "aofrectangle":
                    areaOfRectangle(userinputasnum1, userinputasnum2)
                if userinput == "aofparallelogram":
                    areaOfParallelogram(userinputasnum1, userinputasnum2)
                if userinput == "aoftriangle":
                    areaOfTriangle(userinputasnum1, userinputasnum2)
                    
        elif userinput == "O":
            print("Choose operations in aofsquare, aofrhombus, aofcircle")
            userinput = input()
            if  userinput == "aofsquare" or userinput == "aofrhombus" or userinput == "aofcircle":
                print("Enter first no. ")
                userinputasnum1 = input()
                userinputasnum1 = int(userinputasnum1)
                if userinput == "aofsquare":
                    areaOfSquare(userinputasnum1)
                if userinput == "aofcircle":
                    areaOfCircle(userinputasnum1)
                if userinput == "aofrhombus":
                    areaOfRhombus(userinputasnum1)
        elif userinput != "exit":
            print("Whatever you have given is not a valid operation")
            
        else:
            print("THANKYOUUUUU!!!!!!!")
        
        