# R = int(input("enter the no. of rows: "))

# for row in range(1,R+1):
#     for col in range(1,2*R):

#         if row == row or row+col == R+1 or col-row == R-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
def hollow_triangle(rows, cols):
  """Prints a hollow triangle with rows and cols as variables."""
  for i in range(1, rows + 1):
    for j in range(1, cols + 1):
      if i == 1 or i == rows or j == 1 or j == cols or i + j == rows + 1 or j - i == rows - 1:
        print('*', end='')
      else:
        print(' ', end='')
    print()


hollow_triangle(5, 5)