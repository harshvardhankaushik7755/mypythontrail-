rows = int(input("No. of rows"))
l=input()

while l!= "exit":
    
    for i in range(rows):
        for j in range(rows-i-1):
            print("", end=" ")
            
        for j in range(i + 1):
            print("*", end=" ")
            
        print()
        continue


