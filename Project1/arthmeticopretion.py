def add(a,b):
    sum = a + b
    print("The sum is:", sum)
    
def sub(a,b):
    sub = a - b
    print("The subtraction is:", sub)
    
def mul(a,b):
    mul = a * b
    print("The multiplication is:", mul)
    
def div(a,b):
    div = a / b
    print("The division is:", div)
    
if __name__ == '__main__':
    l=None
    while (l!="exit"):
        print("Choose anyone of the four mathematical opreation: add, sub, mul, div")
        l = input()
        if (l=='add' or l=='sub' or l=='mul' or l=='div'):
            print("Enter the first number: ")            
            a=input()
            print("Enter the second number: ")   
            b = input()
            a = int(a)
            b = int(b)        
            if (l == 'add'):
                add(a,b)
            elif (l == 'sub'):
                sub(a,b)
            elif (l == 'mul'):
                mul(a,b)
            elif (l == 'div'): 
                div(a,b)
        elif(l!= 'exit'):
            print(l +" is not a corect opretion choose another option please")
        else:
            print("THANK YOU FOR USING CALCULATER 2.0")
            continue
