from pynput import keyboard
#from pynput.keyboard import Key, Listener
import time
import sys
import os
import random

recording = False
solvetime = 0

currentScramble = ""

times =[]

moves = ["R", "R'", "B", "B'", "D", "D'", "U", "U'", "F2", "F'", "F", "R2"]

def scramble():
    scramble = ""
    move = ""
    premove = ""
    
    for i in range(10):
        move = random.choice(moves) + " "
        
        while move[0] == premove:
            move = random.choice(moves) + " "
            
        premove = move[0]
        scramble += move
        
    return scramble

currentScramble = scramble()
print("Scramble: " + currentScramble)  

def on_press(key):
    pass

def on_release(key):
    global recording
    global solvetime
    global currentScramble
    
    if key == keyboard.Key.space:
        recording = not recording
        
        if not recording:
            os.system('cls')
            print(f'Finished in {solvetime} Time: {solvetime}')
            f=open('scrambles.txt', 'a')
            f.write(f'\nScramble: {currentScramble} time: {solvetime}')
            f.close()
            currentScramble = scramble()
            print('new scramble: ' + currentScramble)
            times.append(solvetime)
            average = sum(times) / len(times)
            
            print("times: ")
            
            for i in times:
                print("  "+str(i))
                
                print("Average: " + str(average))
                solvetime = 0
                
listener = keyboard.Listener(
    on_press = on_press,
    on_release = on_release
)

listener.start()

while True:
    if recording:
        solvetime += 1
        sys.stdout.write("\rtime: " + str(solvetime))
        sys.stdout.flush()
        time.sleep(1)