
def riddleJapaneseship(answer):
    answer = "The Chinese worker lied and stole captains watch and necklace as Japanese flag is not symmetrrical and cannot be upside down."
    print("Correct answer you detective!!!!!!! you gave the ans :-", answer)

if __name__ == "__main__":
    userans = None
    while userans!= "exit":
        print("Once a Japanese ship was on it's sail to Canada. The captain of the ship went to take a bath , he left his watch and necklace in his room and went to washroom. When he came he found that his watch and necklace were missing. he askes four other crew members. The Israel member said I was in the generator room fixing the  putting a new battery inside. Chinese worker said he was correcting the flag which was placed upside down. The Indian said he was taking butter out and the Afghani said he was preparing chicken for lunch. Whithin some seconds the captain got the theif and punished him. Can you guess who stole captains necklace and watch and how he caught the theif between the four crew members. Give reason to support your answer.")
        userans = input()
        if userans == "The Chinese worker lied and stole captains watch and necklace as Japanese flag is not symmetrical and can't be upside down.":
            riddleJapaneseship(print("Correct answer you detective!!!!!!!"))
        elif userans!= "exit":
            print("Looks like you're wrong or your spellings are not correct :)")
        else:
            print("Thank you!!!!!!")
            
            