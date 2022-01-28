import pyglet
from pyglet.gl import *

from Game import Game

sprite_width = 50
sprite_height = 50
window_width = 700
window_height = 700

path = 'C:/Users/1/Desktop/GAME/'

if __name__ == "__main__":
          window = Game(path, window_width, window_height)
          glClearColor(0.7, 0.9, 1, 1)
          pyglet.app.run()
