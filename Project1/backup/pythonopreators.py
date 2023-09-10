# 1. python arthmatic opreators
a=5
b=2
# addition
def add():
    sum = (a+b)
    print("the sum of a and b is ", sum)
# substraction
    
def sub():
    sub = (a-b)
    print("substraction of a and b is ", sub)
#multiplication    
def mul():
    mul=(a*b)
    print("multiplication of a and b is ", mul)
#division
def div():
    div=(a/b)
    print("division of a and b is ", div)
#floordivision
def fldiv():
    fldiv=(a//b)
    print("floor division of a and b is ", fldiv)
    
#power
def pow():
    pow=(a**b)
    print("power of a and b is ", pow)

#modulo
def mod():
    mod=(a%b)
    print("the modulo of a and b is ", mod)

if __name__ =='__main__':
    add()
    sub()
    mul()
    div()
    fldiv()
    pow()
    mod()