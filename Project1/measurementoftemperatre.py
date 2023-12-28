def convertCentiToFarenheit(tempinCenti):
    tempinFarenheit =  tempinCenti * (9/5) + 32
    print("Temperature in Farenheit: ", tempinFarenheit)
    
def convertFarenToCenti(tempinfaren):
    tempincenti = 5/9 * (tempinfaren -32)
    print("temperature in Celsius: ", tempincenti)

def convertKelvinToCenti(tempinkelvin):
    tempinCenti = tempinkelvin + 273.15
    print("Temperature in Celsius: ", tempinCenti)
    
def convertCentiToKelvin(tempinCenti):
    tempinkelvin = tempinCenti - 273.15
    print("Temperature in Kelvin: ", tempinkelvin)
    
def convertFarnToKelvine(tempinFaren):
    tempinkelvin =  (tempinFaren - 32) * 5 / 9 + 273.15
    print("Temperature in Kelvin: ", tempinkelvin)
    
def convertKelvinToFaren(tempinCenti):
    tempinkelvin = tempinCenti - 273.15
    print("Temperature in Kelvin: ", tempinkelvin)
    

    
    
if __name__ == "__main__":
    userinput = None
    while userinput!= "exit":
        print("Choose the operations in ctof, ftoc, ktoc, ctok, ftok, ktof")
        userinput = input()
        if userinput == "ctof" or userinput=="ftoc" or userinput == "ktoc" or userinput == "ctok" or userinput == "ftok" or userinput == "ktof":
            print("Enter the temperature ")
            userinputastemp = input()
            userinputastemp = int(userinputastemp)
            if userinput == "ctof":
                convertCentiToFarenheit(userinputastemp)
            if userinput == "ftoc":
                convertFarenToCenti(userinputastemp)
            if userinput == "ktoc":
                convertKelvinToCenti(userinputastemp)
            if userinput == "ctok":
                convertCentiToKelvin(userinputastemp)
            if userinput == "ftok":
                convertFarnToKelvine(userinputastemp)
            if userinput == "ktof":
                convertFarnToKelvine(userinputastemp)
                
        elif userinput != "exit":
            print("Wrong selection.")
            
        else:
            print("Thank You for using my temperature calculator.")
                
            
            
        