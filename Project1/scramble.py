import random

scramble = ["R", "R'", "U", "U'", "L", "L'", "B", "B'", "D", "D'", "F", "F'", "R2", "U2", "L2", "B2", "D2", "F2"]
scrambleList = random.choices(scramble, k=20)
print(scrambleList)