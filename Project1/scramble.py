import random
import string

scramble = ("R", "R'", "U", "U'", "L", "L'", "B", "B'", "D", "D'", "F", "F'")
scrambleList = random.choice(string.ascii_letters(scramble), 15)
print(scrambleList)