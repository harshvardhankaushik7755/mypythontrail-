
num = int(input("No. of rows"))

#  

for row in range(1, num+1):
    for col in range(1,num+1):
        if row == 1 or row==num or col==num or col == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()


    
    