def add(a, b):
    sum = a+b
    print("addition = ", sum)
    
def sub(a, b):
    sub = a-b
    print("difference = ", sub)

def mul(a, b):
    mul = a*b
    print("multiplication = ", mul)
    
def div(a, b):
    div = a/b
    print("division = ", div)
    
def square(a, ):
    sq = a*a
    print("square:", sq)
    
def cube(a):
    cube = a*a*a
    print("cube: ", cube)
    
if __name__ == "__main__":
    l = None
    while(l!="exit"):
        l = input()
        print("")
        if (l == "add" or l == "sub" or l=="mul" or l=="div"):
            print("enter first number")
            a = input()
            print("enter second no.(note: if you have taken square or cube operation print the same no. you putted on the first one)")
            b = input()    
            a = int(a)
            b = int(b)
            if l=="add":
                add(a, b)
            if l=="sub":
                sub(a, b)
            if l=="mul":
                mul(a, b)
            if l == "div":
                div(a, b)
                
        elif l=="square" or l=="cube":
            print("enter the number")
            a = input()
            a = int(a)
            if l=="square":
                square(a)
            if l=="cube":
                cube(a)
                
        elif l!="exit":
            print("whatever you have written is not a correct operation")
        else:
            print("THANK YOU FOR USING THIS CALCULATOR")
            break