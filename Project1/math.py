import random
import time

operators = ["=", "-","*"]
min_operaand = 3
max_operand = 12
total_probs = 10

def generate_q():
    left = random.randint(min_operaand, max_operand)
    right = random.randint(min_operaand, max_operand)
    operator = random.choice(operators)
    
    expr = str(left) + " " + operator +  " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press Enter to Start")
print("---------------------------")
start_time = time.time()

for i in range(total_probs):
    expr, answer = generate_q()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong+=1
end_time = time.time()
total_time = round(end_time - start_time, 2)        
print("---------------------------")
print("Nice Work! You finished in ", total_time, "seconds")
