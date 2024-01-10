num = int(input("no. of rows"))

for i in range(1, num+1):
    for j in range(1, num*2):
        if i == num or i+j == num+1 or j-i == num-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print()