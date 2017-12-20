import random
import pygame
from pygame.locals import *

def tõrjumine(x,y,mängija_x,mängija_y):
    if y >= mängija_y - 7.5 and y <= mängija_y + 42.5:
        return True
    return False

def vastu_seina(y):
    if y<= 10 or y>= 457.5:
        return True

#Mängu initsialiseerimine
pygame.init()

#Mänguvälja deklareerimine
aken = pygame.display.set_mode((640, 480), 0, 32) #loob mänguakna
pygame.display.set_caption("Pongimäng")

#Tausta, "mängijate" ja palli loomine
tausta_alus = pygame.Surface((640, 480))
taust = tausta_alus.convert()
taust.fill((0, 0, 0))
bar = pygame.Surface((10, 50))
mängija1 = bar.convert()
mängija1.fill((100, 100, 200))
mängija2 = bar.convert()
mängija2.fill((255, 100, 100))
ringi_pindala = pygame.Surface((30, 30))
ring = pygame.draw.circle(ringi_pindala, (0, 255, 0), (int(10), int(10)), int(10))
pall = ringi_pindala.convert()
pall.set_colorkey((0, 0, 0))

#Mängijate ja palli algasukoha, liikumiskiiruste ja skooride määramine
mängija1_x, mängija2_x = 10, 620
mängija1_y, mängija2_y = 215, 215
palli_x, palli_y = 307, 232
mängija1_liigu, mängija2_liigu = 0, 0
vertikaalne_kiirus, horisonaatlne_kiirus, kiirus_ring = 250, 250, 250
mängija1_skoor, mängija2_skoor = 0, 0

#Kella ja fondi sätted
kell = pygame.time.Clock()
font = pygame.font.SysFont("arial", 40)

#sündmuste paika panemine    
while True:
    for sündmus in pygame.event.get():
        if sündmus.type == KEYDOWN:
            if sündmus.key == K_UP:
                mängija1_liigu = -ai_kiirus
            elif sündmus.key == K_DOWN:
                mängija1_liigu = ai_kiirus
        elif sündmus.type == KEYUP:
            if sündmus.key == K_UP:
                mängija1_liigu = 0
            elif sündmus.key == K_DOWN:
                mängija1_liigu = 0

    #Joonistab kõik asjad aknasse
    aken.blit(taust, (0, 0))
    frame = pygame.draw.rect(aken, (255, 255, 255), Rect((5, 5), (630, 470)), 2)
    aken.blit(mängija1, (mängija1_x, mängija1_y))
    aken.blit(mängija2, (mängija2_x, mängija2_y))
    aken.blit(pall, (palli_x, palli_y))
    aken.blit(font.render(str(mängija1_skoor), True, (255, 255, 255)), (250, 30))
    aken.blit(font.render(str(mängija2_skoor), True, (255, 255, 255)), (380, 30))

    mängija1_y += mängija1_liigu

    #palli liikumine
    aega_kulunud = kell.tick_busy_loop(60) #aeg millisekundites ja 60 fps (tick_busy_loop() kasutab rohkem CPU-d, kuid on täpsem, kui tick())
    aeg = aega_kulunud / 1000.0 #aeg sekundites

    palli_x += vertikaalne_kiirus * aeg
    palli_y += horisonaatlne_kiirus * aeg
    ai_kiirus = kiirus_ring * aeg

    #AI liikumise määramine
    if palli_x >= 305:
        if mängija2_y != palli_y + 7.5:
            if mängija2_y < palli_y + 7.5:
                mängija2_y += ai_kiirus
            if mängija2_y > palli_y - 42.5:
                mängija2_y -= ai_kiirus
        else:
            mängija2_y == palli_y + 7.5
    #Ei lase "mängijatel" mängu piiridest väljuda
    if mängija1_y >= 420:
        mängija1_y = 420
    elif mängija1_y <= 10:
        mängija1_y = 10

    if mängija2_y >= 420:
        mängija2_y = 420
    elif mängija2_y <= 10:
        mängija2_y = 10

    #Kui toimub kokkupõrge palli ja "mängija" vahel, paneb palli vastassuunas liikuma
    if tõrjumine(palli_x, palli_y, mängija1_x, mängija1_y) or tõrjumine(palli_x, palli_y, mängija2_x, mängija2_y):
        if palli_x < 25:
            palli_x = 21
            vertikaalne_kiirus = -vertikaalne_kiirus
        elif palli_x > 610:
            palli_x = 605
            vertikaalne_kiirus = -vertikaalne_kiirus

    #Lisab punkti saanud mängija skoorile punkti juurde
    if palli_x < 5:
        mängija2_skoor += 1
        palli_x, palli_y = 320, 232.5
        mängija1_y, mängija2_y = 215, 215

    elif palli_x > 620:
        mängija1_skoor += 1
        palli_x, palli_y = 307.5, 232.5
        mängija1_y, mängija2_y = 215, 215
        
    #Kokkupõrkel seinaga suunab ta horisontaalselt vastassuunas liikuma
    if vastu_seina(palli_y):
        horisonaatlne_kiirus = -horisonaatlne_kiirus

    pygame.display.update()
