

l = int(input("length="))
b = int(input("breadth="))

for row in range(1, l+1):
    for col in range(1,b+1):
        if row == 1 or row==l or col==b or col == 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()