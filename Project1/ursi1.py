from ursina import *
def update():
    # cube.x += 0.01
    # cube.y += 0.01
    # cube.rotation_x +=1
    # cube.rotation_y =1
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    cube.color = color.rgb(r,g,b)
    cube.rotation_y +=1
    
app = Ursina()
cube = Entity(model = "cube", color = color.red, position=(4,0,0), scale = 3, rotation_x = 10)
app.run()