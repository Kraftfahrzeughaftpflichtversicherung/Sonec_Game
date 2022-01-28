import pyglet
import random
class Ground():
          def __init__(self,
                                 img,
                                 sprite_width,
                                 sprite_height,
                                 window_width,
                                 window_height):
                    self.image =pyglet.image.load(img)
                    self.window_height = window_height
                    self.window_width = window_width
                    self.sprite_width = sprite_width
                    self.sprite_height = sprite_height
          def cut_ground(self):
                    return int(abs(self.point_c[0] - self.point_b[0])+10), int(abs(self.point_c[1] - self.point_d[0]))
          def generate_ground(self):
                    h = self.window_height - self.sprite_height - 5.0
                    w = self.window_width - self.sprite_width - 5.0
                    self.point_a = [0.0, 0.0]
                    self.point_b = [0.0,  random.uniform(0.0, h)]
                    self.point_c = [random.uniform(0.0, w), random.uniform(0.0, h)]
                    self.point_d = [random.uniform(0.0, w), 0.0]
                    self.image.width, self.image.height = 700, self.cut_ground()[1]
                    print(self.cut_ground())
                    
                    return self.image, self.image.width, self.image.height

#class hillock():
#    def __init__(self,
#                img,
#                y_min,
#                window_width):
#        self.window_width = window_width
#        self.x  = random.uniform(100, window_width-100)
#        self.point_a = [random.uniform(100, window_width-100), y_min]
#        self.point_b = [ y_min+random.uniform(20, window_width-300)]



