from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time
import random

game = Ursina()

player = Entity(model= "sphere", color=color.red,  position = (0, 3, -400),scale= (5, 5, 5), collider = "box")
camera.z = -15
camera.add_script(SmoothFollow(target = player, offset = (0, 5, -30)))
road = Entity(model= "plane", color=color.black, scale= (5, 10, 1000000))
bullet = Entity(model = "sphere")
rows = [-15, -10, -5, 0, 5, 10, 15]
median_r = Entity(model= "cube",collider = "box" ,position = (25, 2, 0), scale= (5, 10, 1000000), color=color.white)
median_r = Entity(model= "cube",collider = "box" ,position = (-25, 2, 0), scale= (5, 10, 1000000), color=color.white)
score_board = Text(text = str(0), scale = 5, x = -0.85, y = 0.45)
speed = 200


def update():
    player.z = player.z + time.dt * speed
    player.rotation_x = player.rotation_x + time.dt * 50
    score_val = player.z +600
    score = int(score_val)
    global rows
    if held_keys["d"]:
        player.x = player.x + time.dt * 25
        player.rotation_z = player.rotation_z + time.dt * 100
    if held_keys["a"]:
        player.x = player.x + time.dt * 25
        player.rotation_z = player.rotation_z - time.dt * 100
    if held_keys["a"]:
        player.x = player.x + time.dt * 1000
        player.rotation_x = player.rotation_x - time.dt * 600
        
    if player.intersects().hit or median_r.intersects().hit:
        destroy(game)
        
    score_board = str(score)
    
for i in range(0, 100000, 100):
    enemy = Entity(model = "cube", collider = "box", position = (random.choice(rows), 6, i), color = color.random_color())
    
window.fullscreen = 1
sky = Sky()
game.run                                                 
                          
# player = Entity(model= "cube", color=color.blue, scale_y= 2)
# def update():
#     player.x += held_keys["d"] * 0.1
#     player.x -= held_keys["a"] * 0.1
#     player.x += held_keys["w"] * 0.1
#     player.x -= held_keys["s"] * 0.1
#     player.rotation_x += held_keys["r"] * 5
#     player.rotation_y += held_keys["r"] * 5
    
# app.run()