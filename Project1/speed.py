from time import *
from random import *

def mistake(paratest, usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error+1
        except:
            error = error+1
    return error
        
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput)/time_R
    return round(speed)

    

test = ["how rh egs kgsjgfu were yoy not yesterday wafle",
"me nombre es harshvardhan kaushik", "welcome gjgqjhgd gkgiuyb"]
test1 = random.choice(test)
print("*****Typing speed calculator*****")
print(test1)
print()
print()
time_1 = time()
testinput = input("Enter : ")
time_2 = time()

print("Speed : ",speed_time(time_1,time_2,testinput), " w/sec")
print("Error : ",mistake(test1,testinput))

mistake()
speed_time()