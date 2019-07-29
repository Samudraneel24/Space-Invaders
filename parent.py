from pygame import *
screen = display.set_mode((640, 480))


class parent(object):
    def __init__(self, xp, yp, img):
        self.x = xp
        self.y = yp
        self.bitmap = image.load(img)
        self.bitmap.set_colorkey((0, 0, 0))

    def position(self, xp, yp):
        self.x = xp
        self.y = yp

    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))
