import pyglet
def sprite_type(path='C:/Users/1/Desktop/GAME/', type_ = "standing_right"):
    if type_ == "standing_right":
        sprite = pyglet.image.load(path + 'standing_right.png')
    if type_ == "standing_left":
        sprite = pyglet.image.load(path + 'standing_left.png')
    if type_ == 'jumping_right':
        sprite = pyglet.image.load(path + 'jumping_right.png')
    if type_ == 'jumping_left':
        sprite = pyglet.image.load(path + 'jumping_left.png')
    if type_ == 'running_right':
        sprite = pyglet.image.load(path + 'running_right.png')
    if type_ == 'running_left':
        sprite = pyglet.image.load(path + 'running_left.png')

    return sprite, type_


class Character(pyglet.sprite.Sprite):         
    def __init__(self, img, x, y):
        self.img = img
        return pyglet.sprite.Sprite.__init__(self, img[0], x = 0, y = 0)
    def get_orientation(self):
        if 'right' in self.img[1]:
            return 'right'
        if 'left' in self.img[1]:
            return 'left'

