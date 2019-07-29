from pygame import *
from random import *
import time as ttt
from collision import *
from alien import *
from ship import *
from missile import *

init()
screen = display.set_mode((640, 480))
key.set_repeat(1, 1)
display.set_caption('SpaceInvaders')
backdrop = image.load('data2/backdrop.jpg')
Ship = ship(275, 400, 'data2/ship.png')
white = (255, 255, 255)

q = 0
flag = 0
t = ttt.time()
t2 = ttt.time()
Missile = []
Missile2 = []
d = 1
d2 = 0
fps = time.Clock()
score = 0


def Score(score):
    Font = font.SysFont(None, 40)
    text = Font.render("Score: " + str(score), True, white)
    screen.blit(text, (10, 10))


while q == 0:
    screen.blit(backdrop, (0, 0))
    if ((abs(ttt.time() - t) % 10 <= 0.1) or (flag == 0)) and d == 1:
        temp = ttt.time()
        flag = 1
        row = randint(1, 8)
        col = randint(1, 2)
        enemy = alien1(50 * row, 50 * col, 'data2/alien.jpg')
        d = 0

    if(d == 0):
        enemy.render()
    if((ttt.time() - temp) >= 8) and d == 0:
        del enemy
        d = 1

    for Key in event.get():
        if Key.type == QUIT:
            q = 1
        if Key.type == KEYDOWN:
            if Key.key == K_q:
                q = 1
            if Key.key == K_d and Ship.x < 590:
                Ship.x += 5
            if Key.key == K_a and Ship.x > 10:
                Ship.x -= 5
        if Key.type == KEYUP:
            if Key.key == K_SPACE:
                Missile.append(
                    missile1(Ship.x + 8, Ship.y - 40, 'data2/missile1.jpg'))
            if Key.key == K_s:
                Missile2.append(
                    missile2(Ship.x + 8, Ship.y - 40, 'data2/missile2.jpg'))

    for m in Missile:
        if m.y >= 0:
            m.render()
            m.y -= m.mov
    for m in Missile2:
        if m.y >= 0:
            m.render()
            m.y -= m.mov

    Score(score)

    for m in Missile:
        if m.y > 0:
            if d == 0 and collision(m.x, m.y, enemy.x, enemy.y) == 1:
                del enemy
                del m
                d = 1
                score += 1
            if d2 == 1 and collision(m.x, m.y, enemy2.x, enemy2.y) == 1:
                del enemy2
                del m
                d2 = 0
                score += 1

    for m in Missile2:
        if m.y > 0 and d == 0:
            if collision(m.x, m.y, enemy.x, enemy.y) == 1:
                del enemy
                enemy2 = alien2(50 * row, 50 * col, 'data2/alien2.png')
                t2 = ttt.time()
                d2 = 1
                del m
                d = 1

    if d2 == 1:
        enemy2.render()

    if abs(ttt.time() - t2) >= 5 and d2 == 1:
        del enemy2
        d2 = 0

    fps.tick(60)
    Ship.render()
    display.update()
