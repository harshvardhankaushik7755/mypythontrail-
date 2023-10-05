from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

set = Ursina()
window.exit_button.visible = True
window.fps_counter_enable = False

class level_1_class(Entity):
    def __init__(self, **kwargs):
        self.player = FirstPersonController()
        super().__init__(parent= self.player)
        self.blocks = []
        self.player.position.z = 10
        window.fullscreen = True
        
    def environment(self):
        Sky(texture = "sky_default")
        self.ground = Entity(model = "plane" ,texture = "grass", collider = "mesh", scale = Vec3(100, 1, 100))

def window_choice(choice):
   if choice == "Level 1":
       level1 = level_1_class()
       level1.environment()
       
window_choice("level 1")


set.run()