import random


play_game = "y"
start = 1
end = 100
direction = "N"
smallest = start
highest = end

while play_game == "y":
    smallest = start
    highest = end
    print("guess a number between 1 and 100: ")
    try_number = random.randint(start, end)
    print(try_number)
    counter = 0
    direction = "N"
    
    while direction != "C":
        direction = input("Is it large (L), is it small (S), or correct(C)?")
        if direction == "S":
            if try_number > smallest:
                smallest = try_number + 1
                try_number = random.randint(smallest, highest)
                print(try_number)

        elif direction == "L":            
            if try_number < highest:
                smallest = try_number - 1
                try_number = random.randint(smallest, highest)
                print(try_number)
                try_number = random.randint(smallest, highest)
                print(try_number)
        counter = counter + 1
        
print("Yes I did it in" + str(counter) + "times.")
play_game = input("Continue ?")
