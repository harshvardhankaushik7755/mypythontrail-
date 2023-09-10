import time
import pyttsx3
from plyer import notification
AI = pyttsx3.init()

print("Welcome to Tatti reminder app.")
print("Enter ctrl + c to exit the program")

name = input("Enter your name(0 to exit)")
print("1 Hour = 3600 seconds")
tym = int(input("how many seconds for reminder"))
while True:
    if(name == '0'):
        AI.say("You have exited the program")
        AI.runAndWait
        break
    else:
        time.sleep(tym)
        notification.notify(
            title='reminder',
            message=f"You need to take a break {name}",
            timeout=3
        )
        AI.say(f"You gotta drink water {name}")
        AI.runAndWait()
        