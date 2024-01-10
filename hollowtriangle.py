R = int(input("enter the no. of rows: "))

for row in range(1,R+1):
    for col in range(1,2*R):

        if row == R or row+col == R+1 or col-row == R-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()