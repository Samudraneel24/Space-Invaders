from parent import *


class missile1(parent):
    def __init__(self, xp, yp, img):
        super(missile1, self).__init__(xp, yp, img)
        self.mov = 1


class missile2(parent):
    def __init__(self, xp, yp, img):
        super(missile2, self).__init__(xp, yp, img)
        self.mov = 2
