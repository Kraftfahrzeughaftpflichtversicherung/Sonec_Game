import pyglet
from pyglet.window import key

from Ground import Ground
from Character import Character
from Character import sprite_type
import time
class Game(pyglet.window.Window):
          def __init__(self, path, window_width, window_height):
                    self.w = False
                    self.a = False
                    self.s = False
                    self.d = False
                    self.space = False
                    self.dist = 10
                    self.path = path
                    self.grass =pyglet.image.load(self.path+'grass.png')
                    self.background = pyglet.image.load(self.path+'Green_Hill_Zone.png')
                    pyglet.window.Window.__init__(self, width = window_width, height = window_height)
                    self.ground, self.x_min, self.y_min = Ground(self.path + 'ground2.png',
                                         sprite_width=50,
                                 sprite_height=50,
                                 window_width=500,
                                 window_height=500).generate_ground()
                    self.x = 0
                   
                    self.y = self.y_min

                    self.Player = Character(sprite_type(), self.x, self.y)
                    self.Player.update(self.x, self.y)
                    self.Player.scale = 0.5
                    self.schedule = pyglet.clock.schedule_interval(func = self.move, interval = 0.01/60.)
                   
          def on_draw(self):
                    self.clear()
                    self.background.blit(0,0)
                    self.Player.draw()
                    self.ground.blit(0,0)
                    self.grass.blit(0,self.y_min-50)
                    
          
          def on_key_press(self, symbol, modifiers):
            if symbol == key.SPACE:
                self.space = True
                self.Player.update(self.x, self.y)
                self.Player = Character(sprite_type(self.path, 'jumping_'+self.Player.get_orientation()),
                                        self.x, self.y)
                pyglet.clock.unschedule(self.jump)
                pyglet.clock.schedule_interval(func = self.jump, interval = 0.001/60)
                self.Player.update(self.x, self.y)
                self.Player.scale = 0.3
            elif symbol == key.A:
                self.a = True
                self.Player =  Character(sprite_type(self.path, 'running_left'), self.x, self.y)
                self.Player.update(self.x, self.y)
                self.Player.scale = 0.4
            elif symbol == key.D:
                self.d = True
                self.Player =  Character(sprite_type(self.path, 'running_right'), self.x, self.y)
                              
                self.Player.update(self.x, self.y)
                self.Player.scale = 0.4
            
                

                    
          def on_key_release(self, symbol, modifiers):
                    if symbol == key.SPACE:
                            self.Player =  Character(sprite_type(self.path, 'jumping_'+self.Player.get_orientation()), self.x, self.y)
                            self.Player.scale = 0.3
                            self.Player.update(self.x, self.y)
                    elif symbol == key.A:
                              self.Player =  Character(sprite_type(self.path, 'standing_left'), self.x, self.y)
                              self.Player.update(self.x, self.y)
                              self.Player.scale = 0.5
                              self.a = False
                    elif symbol == key.D:
                              self.d = False
                              self.Player =  Character(sprite_type(self.path, 'standing_right'), self.x, self.y)
                              self.Player.update(self.x, self.y)
                              self.Player.scale = 0.5
                    

                    
          def move(self, dt):
            if self.a == True:
                self.x -= self.dist
                self.Player.x -= self.dist
            elif self.d:
                self.x += self.dist
                self.Player.x += self.dist
            elif self.space:
                self.y += 400
                self.Player.y += 400
                self.space = False
          def jump(self, dt):
            
            if self.Player.y > self.y_min:
                self.Player.y -=20
                self.y-=20
               



                  


                    
  
