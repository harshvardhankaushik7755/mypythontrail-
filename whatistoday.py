def DAYS(userinput):
    if userinput == "1st January":
        print("HAPPY NEW YEAR")
    elif userinput == "2nd January":
        print("HAPPPY INTROVERT DAY")
    elif userinput == "3rd January":
        print("HAPPY INTERNATIONAL MIND-WELLNESS AND BODY DAY")
    elif userinput == "4th January":
        print("WORLD BRAILIE DAY")
    elif userinput == "5th January":
        print("HAPPY NATIONAL BIRD DAY")
    elif userinput == "6th January":
        print("HAPPY CALENDER DAY")
        
    
        
        
if __name__ == "__main__":
    userinput = None
    while userinput!="exit":
        print("WRITE YOUR B'DAY DATE OR ANY DATE YOU WANT")
        userinput = input()
        DAYS(userinput)
        