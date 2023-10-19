def add(a, b):
    sum = a+b
    print("sum:", sum)
    
def sub(a, b):
    sub = a-b
    print("substraction: ", sub)
    
def mul(a, b):
    mul = a*b
    print("multiplication:", mul)
    
def div(a, b):
    div = a/b
    print("division:", div)
    
if __name__ == "__main__":
    l = None
    while(l!="exit"):
        print("choose anyone out of the four mayhematical operations: add, sub, mul, div")
        div
        l = input()       
        if (l=='add' or l=='sub' or l=='mul' or l=='div'):
            print("Enter a number: ")
            a = input()
            print("Enter second number: ")
            b = input()
            a = int(a)
            b = int(b)
            if l == "add":
                add(a, b)
            elif l == "sub":
                sub(a, b)
            elif l == "mul":
                mul(a, b)
            elif l == "div":
                mul(a, b)
        elif(l!="exit"):
            print(l+" is not a correct option!!")
        else:
            print("THANKYOU FOR USING MY CALCULATOR")
            break