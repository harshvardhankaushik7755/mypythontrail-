# Add two no.'s given by the user
def add(a,b):
    sum = a + b
    print("The sum is:" , sum) 
    
# Subtract two no.'s given by the user
def sub(a,b):
    sub = a - b
    print("The subtraction is:", sub)
    
    # Multiply two no.'s given by the user
def mul(a,b):
    mul = a * b
    print("The multiplication is:", mul)
    
    # divide two no.'s given by the user
def div(a,b):
    div = a / b
    print("the quotient is:", div)    

if __name__ == '__main__':
    q=None
    while (q!='exit'):
        print("Choose anyone of the four mathematical opreation: add, sub, mul, div")
        q = input()    
        if (q != "exit"):
            print("Enter the first number:")
            a=input()
            print("Enter the second number:")    
            b = input()   
            
            a=int(a)
            b=int(b)
            
            if (q == 'add'):
                add(a,b)
            elif (q == 'sub'):
                sub(a,b)
            elif (q == 'mul'):
                mul(a,b)
            elif (q == 'div'): 
                div(a,b)
            else:
                print(q +" is not a correct option")