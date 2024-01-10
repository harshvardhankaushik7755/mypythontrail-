num = int(input("Enter the no. of rows"))

for row in range(1, num+1):
    for col in range(1, num+1):
        if row == 1 or row == num or col == 1 or col == num:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()