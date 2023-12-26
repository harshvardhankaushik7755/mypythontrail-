import math 
from fractions import Fraction

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
    
def sqrt(a):
    square_root = math.ceil(a ** (1/2))
    print("Square root : ", square_root)
    
def cube_root(a):
    cuberoot = math.ceil(a ** (1/3))
    print("Cube root: ", cuberoot)
    
def pow(a, b):
    power = math.pow(a, b)
    print("power: ", power)
    
def percentage(a, b):
    percent = a/b*100
    print("percentage: ", percent, "%")
    
def root(a, b):
    root = math.pow(a, 1/b)
    print("root: ", root) 
    
def floor(a, b):
    flor =a//b
    print("floor: ", flor)
    
def frac_add(a, b):
    a= Fraction(input())
    b = Fraction(input())
    add = a+b
    print("Sum of fractions: ", add)
    
if __name__ == "__main__":
    l = None
    while(l!="exit"):
        print("If your operation requires a single parametre press 'O', if multi parametre operation press 'M'")
        l = input()
        if l == "M":
            print("Choose any one operation from :'add', 'sub', 'mul', 'div', 'percentage', 'power', 'root', 'floor', 'addition of fractions'")
            l = input()
            if(l == "add" or l == "sub" or l=="mul" or l=="div" or l=="percentage" or l=="power" or l == "root" or l== "floor" or l=="addition of fractions"):
                
                print("Enter first no:, if percent take part of the whole no.")
                a = input()
                print("Enter second no:, if percent whole no.")
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
                if l=="percentage":
                    percentage(a, b)
                if l=="power":
                    pow(a, b)
                if l == "root":
                    root(a, b)
                if l=="floor":
                    floor(a, b)
                    
                if l == "addition of fractions":
                    frac_add(a, b)
                    
        elif l == "O":
            print("Chose operations in cube, square, cube_root, sqrt and power")
            l = input()    
            if l=="square" or l=="cube" or l== "sqrt" or l =="cube_root" or l=="power":
                print("enter the number")
                a = input()
                a = int(a)
                if l=="square":
                    square(a)
                if l=="cube":
                    cube(a)
                if l=="sqrt":
                    sqrt(a)
                if l=="cube_root":
                    cube_root(a)
                    
                
        elif l!="exit":
            print("whatever you have written is not a correct operation")
            
        else:
            print("THANK YOU FOR USING THIS CALCULATOR")
            break