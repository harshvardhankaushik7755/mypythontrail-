
# Children (00-14 years)
# Youth (15-24 years)
# Adults (25-64 years)
# Seniors (65-100 years )
# Centenarians: (101-110 years )
# supercentarians: (111 and above years )

# Operator	Meaning	Example
# ==	Is Equal To	3 == 5 gives us False
# !=	Not Equal To	3 != 5 gives us True
# >	Greater Than	3 > 5 gives us False
# <	Less Than	3 < 5 gives us True
# >=	Greater Than or Equal To	3 >= 5 give us False
# <=	Less Than or Equal To	3 <= 5 gives us True


def getage(age):
    if (age>0 and age<=14):
        print("You are a child")
    elif (age>14 and age<=24):
        print("you are a Youth")            
    elif (age>24 and age<=64):
        print ("You are an adult")    
    elif (age>64 and age<=100):
        print("You are an teenager/kid")
    elif (age>100 and age<=110):
        print("you are a centarian")
    elif (age>110):
        print("you are a supercentarian")

def getgender(gen):
    print("Your gender is ", gen)
    
def depositmoney(mon):
    print(mon+" rupees deposited")

 
if __name__=='__main__':
    fun = None
    while (fun!='exit'):
        print("Choose anyone of the four opreation: getage,getgender,depositmoney")
        fun = input()        
        if (fun=='getage' or fun=='getgender' or fun=='depositmoney'):
            if(fun =='getage'):
                print("Enter your age:")
                age = input()
                age=int(age)
                getage(age)
            elif(fun =='getgender'):
                print("Enter your gender:")
                gen = input()
                getgender(gen)
            elif(fun=='depositmoney'):
                print("How much money do you want to deposit?")
                mon = input()
                depositmoney(mon)
            
        elif (fun!='exit'):
            print("The value you have given is not the correct option")
        else:             
            print("THANK YOU FOR USING AGE DECIDER")
            continue