import json

def occasionOfDay(input):
    print(input)   

        
if __name__ == "__main__":
    with open("occasion.json", "r") as jsonfile:
        data = json.load(jsonfile)
    # print(data)
    userinput = None
    while userinput!="exit":
        userdate = input()
        occasionOfDay(data[userdate])
        