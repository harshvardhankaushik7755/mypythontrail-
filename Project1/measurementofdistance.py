def convertKilometremToMetre(inputinkm):
    inmetre = inputinkm*1000
    print("Distance in metres: ", inmetre, "m")
    
def convertMetreToCentimetre(inputinm):
    incm = inputinm*100
    print("Distance in cm :", incm, "cm")
    
def convertCentimetreToMillimetre(inputincm):
    inmm = inputincm*10
    print("Distance in in mm(millimetre): ", inmm, "mm")
    
def convertMetretoKilometre(inputinm):
    inkilometre = inputinm/1000
    print("Distance in km: ", inkilometre, "km")
    
def convertCentimetreToMetre(inputincm):
    inmetre = inputincm/100
    print("Distance in metre: ", inmetre, "m")
    
def convertMillimetreToCentimetre(inputinmm):
    incm = inputinmm/10
    print("Distance in mm: ", incm, "cm")
    
if __name__ == "__main__":
    userinput = None
    while userinput!="exit":
        print("Choose any operartions in :- cmtomm, mmtocm, kmtom, mtokm, mtocm, cmtom")
        userinput = input()
        if userinput == "cmtomm" or userinput == "mmtocm" or userinput == "kmtom" or userinput == "mtokm" or userinput == 'mtocm' or userinput == "cmtom":
            print("Enter the no.: ")
            userinputasnum = input()
            userinputasnum = int(userinputasnum)
            if userinput == "cmtom":
                convertCentimetreToMetre(userinputasnum)
            if userinput == "cmtomm":
                convertCentimetreToMillimetre(userinputasnum)
            if userinput == "kmtom":
                convertKilometremToMetre(userinputasnum)
            if userinput == "mmtocm":
                convertMillimetreToCentimetre(userinputasnum)
            if userinput == "mtocm":
                convertMetreToCentimetre(userinputasnum)
            if userinput == "mtokm":
                convertMetretoKilometre(userinputasnum)
        elif userinput != "exit":
            print("Whatever you have written is not a valid operation")
            
        else:
            print("Thankyou for using my measurement calculator")