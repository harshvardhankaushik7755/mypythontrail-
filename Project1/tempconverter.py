def ctof(a):
    c= a
    f= (c * 9/5) + 32
    print("The value you have given in celsius is", f)
    
def ftoc(a):
    f= a
    c= (f - 32) * 5/9
    print("The value you have given in farenheit is", c)
    
def ktof(a):
    k= a
    f= ( k- 273.15) * 9/5 + 32
    print("The value you have given in kelvin is", f)
    
def ktoc(a):
    k= a
    c= k - 273.15 
    print("The value you have given in kelvin is", c)
    
def ftok(a):
    f= a
    k= (f - 32) * 5/9 + 273.15
    print("The value you have given in farenheit is", k)
    
def ftok(a):
    c= a
    k= (c - 32) * 5/9
    print("The value you have given in celsius is", k)
    
if __name__ == '__main__':
    q = None
    while (q!='exit'):
        print("Choose any converstion you want to do: ctof, ftoc, ktof, ktoc, ctok, ftok ")
        q=input()
        if (q == 'ctof' or q == 'ftoc' or q == 'ktof' or q == 'ktoc' or q == 'ctok' or q == 'ftok'):
            print("Enter the number:")
            a=input()
            a = int(a)
            if (q == 'ctof'):
                ctof(a)
            elif (q == 'ftoc'):
                ftoc(a)
            elif (q == 'ktoc'):
                ktoc(a)
            elif (q == 'ktof'):
                ktof(a)
            elif (q == 'ftok'):
                ktoc(a)
            elif (q == 'ctok'):
                ktof(a)
        elif(q!='exit'):
            print(q +"is not the correct option for converstion")
        else:
            print("THANKS")
                
            
    