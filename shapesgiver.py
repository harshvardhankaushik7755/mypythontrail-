

def square(rows):
    print("Solid square: ")
    for i in range(1, rows): 
          
        for j in range(1, rows + 1): 
            print("*", end = " ") 
  
        print() 
        
def rect(l, b):
    print("Solid rect: ")
    for row in range(1, l+1):
        for col in range(1,b+1):
            if row == 1 or row==l or col==b or col == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()
        
        
def triangle(rows):
    for i in range(rows):
            for j in range(rows-i-1):
                print("", end=" ")
                
            for j in range(i + 1):
                print("*", end=" ")
                
            print()
        
triangle(6)

def hollowsquare(num):
    print("Hollow square: ")
    for row in range(1, num+1):
        for col in range(1,num+1):
            if row == 1 or row==num or col==num or col == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()
        
def hollowrectangle(l ,b):
    for row in range(1, l+1):
        for col in range(1, b+1):
            if row == 1 or row == l or col == b or col == 1:
                print("*", end=" ")
                
            else:
                print(" ", end=" ")
                
        print()
        
def hollowtriangle(num):
    for i in range(1, num+1):
        for j in range(1, num*2):
            if i == num or i+j == num+1 or j-i == num-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
                
        print() 
        
        
if __name__ == "__main__":
    userinput = None
    while userinput!="exit":
        print("If your shape is hollow then write H, if solid write S.")
        userinput = input()
        if userinput == "H":
            print("if your operation requires 1 parametre press O if two press M")
            userinput = input()
            if userinput == "M" or "O":
                print("choose the shape 'hollow triangle' or 'hollow square'")
                userinput = input()
                if userinput == "hollow triangle" or userinput == "hollow square":
                    print("enter the no. of rows")
                    userinputasnum = input()
                    userinputasnum = int(userinputasnum)
                    if userinput == "hollow triangle":
                        hollowtriangle(userinputasnum)
                    elif userinput == "hollow square":
                        hollowsquare(userinputasnum)
                        
                print("choose the shapes in hollow rectangle")
                userinput = input()
                if userinput == "hollow rectangle":
                    print("Enter the length")
                    userinputasnum1 = input()
                    print("Enter the breadth")
                    userinputasnum2 = input()
                    userinputasnum1 = int(userinputasnum1)
                    userinputasnum2 = int(userinputasnum2)
                    if userinput == "hollow rectangle":
                        hollowrectangle(userinputasnum1, userinputasnum2)
                        
        if userinput == "S":
            print("if your operation requires 1 parametre press O if two press M")
            userinput = input()
            if userinput == "O" or "M":
                print("choose the shape 'solid triangle' or 'solid square'")
                userinput = input()
                if userinput == "solid triangle" or userinput == "solid square":
                    print("enter the no. of rows")
                    userinputasnum = input()
                    userinputasnum = int(userinputasnum)
                    if userinput == "solid triangle":
                        triangle(userinputasnum)
                    elif userinput == "solid square":
                        square(userinputasnum)

                print("choose the shapes in solid rectangle")
                userinput = input()
                if userinput == "solid rectangle":
                    print("Enter the length")
                    userinputasnum1 = input()
                    print("Enter the breadth")
                    userinputasnum2 = input()
                    userinputasnum1 = int(userinputasnum1)
                    userinputasnum2 = int(userinputasnum2)
                    if userinput == "solid rectangle":
                        rect(userinputasnum1, userinputasnum2)
                        
            
        elif userinput!="exit":
            print("Wrong input")
            
        else:
            print("THANK YOUUU")