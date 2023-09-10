#kg to lbs
def kgtolbs(a):
    kg = a
    lbs = kg*(2.205)
    print(kg, " in lbs is ", lbs)
    
def kgtogr(a):
    kg = a
    gr= kg*(1000)
    print(kg, " in grams is ", gr)
    
def grtokg(a):
    kg = a
    gr = kg/(1000)
    print(gr, " in grams is ", kg)
    
def grtomlg(a):
    gr = a
    mlg = gr*(1000)
    print(gr, " in milligrams is ", mlg)
    
def tontokg (a):
    ton = a
    kg = ton*(1000)
    print(ton, " in grams is ", kg)
       
    if __name__ == '__main__':
     p=None
     while (p!='exit'):
        print("Choose anyone of the four mathematical opreation: gramtokg, kgtogram, kgtolbs")
        p=input()
        if (p=='kgtolbs' or p=='kgtogr' or p=='grtokg') :
            print("enter the number: ")
            a=input()
            a=int(a)
            if (p == 'kgtolbs'):
                kgtolbs
            elif (p == 'kgtogr'):
                kgtogr
            elif (p == 'grtokg'):
                grtokg
            elif(p!= 'exit'):
                print(p +" is not a correct option for coversion")
        
        else:
            print("thanks")
                    
                
                       
            
    
    