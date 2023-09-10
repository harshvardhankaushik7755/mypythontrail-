# Add 2 Number
def addnumbers(): #defining a function which add two numbers
    a = 10           #declearing and intiallizing,assign variable
    b = 20
    sum = a + b
    print("The sum is:", sum)

# Subtract 2 Number
def subtractnumber():
    a = 10
    b = 20
    sub = b - a
    print("The substraction is:", sub)

# Multiply 2 Number
def multiplynumber():
    a = 10
    b = 20
    c = 30
    mul = a * b * c
    print("The multiplication is:", mul)

# Divide 2 Number
def dividenumbers():
    a = 10
    b = 20
    div = b / a
    print("The division is:", div)
    
# Modulo 2 Number
def modulonumbers():
    a = 10
    b = 20
    mod = b % a
    print("The modulo is:", mod)
    
    # percentage 1 no.
def percentagenumber():
    totalmarks = 100
    markssecured = 50
    percentage =  (markssecured / totalmarks)* 100
    print("The percentage is:", percentage)
    
if __name__ == '__main__':
      addnumbers()  #Calling a fubction
      subtractnumber()
      multiplynumber()
      dividenumbers()
      modulonumbers()
      percentagenumber()