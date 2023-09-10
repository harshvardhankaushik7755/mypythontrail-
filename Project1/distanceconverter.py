def kmtomi(a):
    km=a                                            
    miles = (0.621371192)*km       #opreator, loop, conditional statements#
    print("The value you have given in kms is", miles)  
    
def fttoin(a):
    ft = a                                                 
    inch = (12)*ft
    print("The value you have given in feet is", inch, "inches")
    

    
def kmtoya(a):
    km = a                                                 
    yards = (1093.61)*km
    print("The value you have given in kilometres is", yards, "yards")
    
def mtonm(a):
    mm = a                                                 
    nm = (1093.61)*mm
    print("The value you have given in nanometres is", nm, "millimetres")
             
def mmtonm(a):
    km=a                                            
    miles = (0.621371192)*km       #opreator, loop, conditional statements#
    print("The value you have given in kms is", miles)                                                                             

if __name__ == '__main__':
    q = None
    while (q!='exit'):
        print("Choose anyone of the opreation you want to do: kmtoya(km to yards), kmtomi(km to miles), fttoin(feet to inch), mmtonm(metre to nanometre)")
        q = input()
        if (q == 'kmtoya' or q == 'kmtomi' or q == 'fttoin'):
            print("Enter the first number:")
            a=input()
            a=int(a)
            if (q == 'kmtoya'):
                kmtoya(a)
            elif (q == 'kmtomi'):
                kmtomi(a)            
            elif (q == 'fttoin'): 
                fttoin(a)
            elif (q =='mmtonm'):
                mmtonm(a)
        elif(q!= 'exit'):
            print(q +" is not a correct option for coversion")
        
        else:
            print("thanks")
                    

                                                                        