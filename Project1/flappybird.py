from ursina import *

app = Ursina()
Sky()
bird = Animation("C:\\Users\\Nandani\\Desktop\\PythonCode\\flappybird.png", collider = "box", scale = (2, 2, 2), y = 5)
camera.orthographic = True
camera.fov = 20

def update():
    bird.y = bird.y - 4 * time.dt
    for pipe in pipes:
        p.x = p.x - 2 * time.dt
    
def input(key):
    if key == "space":
        bird.y = bird.y + 3
        
pipes = []
pipe = Entity(model = "quad", color = color.green, texture = "white_cube", position = (20, 10), scale = (3, 15, 1), collider = "box")
import random as r
def new_pipe():
    y = random.randint(4, 12)
    new1 =  duplicate(pipe, y=y)
    new2 = duplicate(pipe, y=y-22)
    pipes.extend((new1, new2))
    invoke(new_pipe, delay= 5)
    
new_pipe()
app.run()
    
    
