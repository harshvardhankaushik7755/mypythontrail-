

def square(rows, col):
    print("Solid square: ")
    for i in range(1, rows): 
          
        for j in range(1, col + 1): 
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
        
        
def triangle(rows, col):
    for i in range(rows):
            for j in range(col-i-1):
                print("", end=" ")
                
            for j in range(i + 1):
                print("*", end=" ")
                
            print()
        

def hollowsquare(row, col):
    print("Hollow square: ")
    for i in range(1, row+1):
        for j in range(1,col+1):
            if row == 1 or row==i or col==j or col == 1:
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
        
def hollow_triangle(n):
  
    for i in range(1, n + 1):
        for j in range(1, 2 * n):
            if i == n or i + j == n + 1 or j - i == n - 1:
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
                print("choose the shape or 'hollow square' or 'hollow rectangle'")
                userinput = input()
                if userinput == "hollow square" or userinput == "hollow rectangle":
                    print("enter the no. of rows")
                    userinputasnum1 = input()
                    userinputasnum1 = int(userinputasnum1)
                    print("Enter the no. of cols: ")
                    userinputasnum2 = input()
                    userinputasnum2 = int(userinputasnum2)
                    if userinput == "hollow square":
                        hollowsquare(userinputasnum1, userinputasnum2)
                    elif userinput == "hollow rectangle":
                        hollowrectangle(userinputasnum1, userinputasnum2)
                if userinput == "hollow triangle":
                    print("enter the no.")
                    userinputasnum1 = input()
                    userinputasnum1 = int(userinputasnum1)
                    if userinput == "hollow triangle":
                        hollow_triangle(userinputasnum1)
                    
                    
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
            userinput = input()
            print("choose the shape 'solid triangle' or 'solid square' or 'solid rectangle'")
            userinput = input()
            if userinput == "solid triangle" or userinput == "solid square" or userinput == "solid rectangle":
                print("enter the no. of rows")
                userinputasnum1 = input()
                userinputasnum1 = int(userinputasnum1)
                print("enter the no. of cols")
                userinputasnum2 = input()
                userinputasnum2 = int(userinputasnum2)
                if userinput == "solid triangle":
                    triangle(userinputasnum1, userinputasnum2)
                elif userinput == "solid square":
                    square(userinputasnum1, userinputasnum2)
                elif userinput == "solid rectangle":
                    rect(userinputasnum1, userinputasnum2)

                        
        elif userinput!="exit":
            print("Wrong input")
            
        else:
            print("THANK YOUUU")