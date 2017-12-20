import random
import pygame
from pygame.locals import *
from sys import exit

#Mängu initsialiseerimine
pygame.init()

#Mänguvälja deklareerimine
ekraan = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Pongimäng")
taust = pygame.Surface((640, 480))
kardin = taust.convert()
kardin.fill((0, 0, 0))
bar = pygame.Surface((10, 50))
mängija1 = bar.convert()
mängija1.fill((100, 100, 200))
mängija2 = bar.convert()
mängija2.fill((255, 100, 100))
ringipindala = pygame.Surface((30, 30))
circ = pygame.draw.circle(ringipindala, (0, 255, 0), (int(10), int(10)), int(10))
pall = ringipindala.convert()
pall.set_colorkey((0, 0, 0))
mängija1_x, mängija2_x = 10, 620
mängija1_y, mängija2_y = 215, 215
palli_x, palli_y = 307, 232
mängija1_move, mängija2_move = 0, 0.
vertikaalne_kiirus, horisonaatlne_kiirus, speed_circ = 250, 250, 250
mängija1_skoor, mängija2_skoor = 0, 0
# clock and font objects
kell = pygame.time.Clock()
font = pygame.font.SysFont("calibri", 40)

def tõrjumine(x,y,mängija_x,mängija_y):
    if y >= mängija_y - 7.5 and y <= mängija_y + 42.5:
        return True
    return False
def vastu_seina(y):
    if y<= 10 or y>= 457.5:
        return True
while True:
    for sündmus in pygame.event.get():
        if sündmus.type == QUIT:
            exit()
        if sündmus.type == KEYDOWN:
            if sündmus.key == K_UP:
                mängija1_move = -ai_speed
            elif sündmus.key == K_DOWN:
                mängija1_move = ai_speed
        elif sündmus.type == KEYUP:
            if sündmus.key == K_UP:
                mängija1_move = 0.
            elif sündmus.key == K_DOWN:
                mängija1_move = 0.

    ekraan.blit(kardin, (0, 0))
    frame = pygame.draw.rect(ekraan, (255, 255, 255), Rect((5, 5), (630, 470)), 2)
    middle_line = pygame.draw.aaline(ekraan, (255, 255, 255), (330, 5), (330, 475))
    ekraan.blit(mängija1, (mängija1_x, mängija1_y))
    ekraan.blit(mängija2, (mängija2_x, mängija2_y))
    ekraan.blit(pall, (palli_x, palli_y))
    ekraan.blit(font.render(str(mängija1_skoor), True, (255, 255, 255)), (250., 30.))
    ekraan.blit(font.render(str(mängija2_skoor), True, (255, 255, 255)), (380., 30.))

    mängija1_y += mängija1_move

    # movement of circle
    time_passed = kell.tick(30)
    time_sec = time_passed / 1000.0

    palli_x += vertikaalne_kiirus * time_sec
    palli_y += horisonaatlne_kiirus * time_sec
    ai_speed = speed_circ * time_sec
    # AI of the computer.
    if palli_x >= 305.:
        if not mängija2_y == palli_y + 7.5:
            if mängija2_y < palli_y + 7.5:
                mängija2_y += ai_speed
            if mängija2_y > palli_y - 42.5:
                mängija2_y -= ai_speed
        else:
            mängija2_y == palli_y + 7.5

    if mängija1_y >= 420:
        mängija1_y = 420
    elif mängija1_y <= 10:
        mängija1_y = 10.
    if mängija2_y >= 420:
        mängija2_y = 420
    elif mängija2_y <= 10:
        mängija2_y = 10
    if tõrjumine(palli_x,palli_y,mängija1_x,mängija1_y) or tõrjumine(palli_x,palli_y,mängija2_x,mängija2_y):
        if palli_x < 25:
            palli_x=20
            vertikaalne_kiirus = -vertikaalne_kiirus
        elif palli_x>610:
            palli_x=605
            vertikaalne_kiirus = -vertikaalne_kiirus

    if palli_x < 5.:
        mängija2_skoor += 1
        palli_x, palli_y = 320., 232.5
        mängija1_y, bar_2_y = 215., 215.
    elif palli_x > 620.:
        mängija1_skoor += 1
        palli_x, palli_y = 307.5, 232.5
        mängija1_y, mängija2_y = 215., 215.
    if vastu_seina(palli_y):
        horisonaatlne_kiirus = -horisonaatlne_kiirus

    pygame.display.update()
