
num = int(input("No. of rows"))

#  
def hollowSquare(rows):
    print("Hollow square: ")
    for row in range(1, num+1):
        for col in range(1,num+1):
            if row == 1 or row==num or col==num or col == 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()
    
    
def solidSquare(rows): 
    print("Solid square: ")
    for i in range(1, rows): 
          
        for j in range(1, rows + 1): 
            print("*", end = " ") 
  
        print() 
        
        
solidSquare(num)
hollowSquare(num)

