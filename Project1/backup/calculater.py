# Add two no.'s given by the user
def addtwonumbers(a,b):
    sum = a + b
    print("The sum is:" , sum) 
    
# Subtract two no.'s given by the user
def subtracttwonumbers(a,b):
    sub = a - b
    print("The subtraction is:", sub)
    
    # Multiply two no.'s given by the user
def multiplytwonumbers(a,b):
    mul = a * b
    print("The multiplication is:", mul)
    
    # divide two no.'s given by the user
def dividetwonumbers(a,b):
    div = a / b
    print("the quotient is:", div)    

if __name__ == '__main__':
    print("Enter the first number:")
    a=input()
    print("Enter the second number:")    
    b = input()    
    a=int(a)
    b=int(b)
    
    addtwonumbers(a,b)
    subtracttwonumbers(a,b)
    multiplytwonumbers(a,b)
    dividetwonumbers(a,b)
