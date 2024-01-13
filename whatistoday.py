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
    elif userinput == "7th January":
        print("HAPPY OLD ROCK DAY")
    elif userinput == "8th January":
        print("HAPPY EARTH ROTATION DAY")
    elif userinput == "9th January":
        print("HAPPY PRAVASI BHARATIYA DIVAS")
    elif userinput == "10th January":
        print("HAPPY WORLD HINDI DAY")
    elif userinput == "11th January":
        print("HAPPY NATIONAL MILK DAY")
    elif userinput == "12th January":
        print("HAPPY SWAMI VIVEKANANDA JAYANTI")
    elif userinput == "13th January":
        print("HAPPY LOHRI AND THE DATE OF THIS PROJECT STARTING")
    elif userinput == "14th January":
        print("HAPPY MAKAR SANKRANTI")
    elif userinput == "15th January":
        print("HAPPY NATIONAL DAY")
        
if __name__ == "__main__":
    userinput = None
    while userinput!="exit":
        print("WRITE YOUR B'DAY DATE OR ANY DATE YOU WANT")
        userinput = input()
        DAYS(userinput)
        