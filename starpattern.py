stars = [['*' for i in range(6)] for j in range(6)]

for i in range(1, 5):
  for j in range(1, 5):
    stars[i][j] = ' '

for i in range(6):
  for j in range(6):
    print(stars[i][j], end='')
  print()