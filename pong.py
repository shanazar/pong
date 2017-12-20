import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

aken = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("Pinks")


taustaks = pygame.Surface((640,480))
taust = taustaks.convert()
taust.fill((0,0,0))
post = pygame.Surface((10,50))
mangija = post.convert()
mangija.fill((255,255,255))
vastane = post.convert()
vastane.fill((255,255,255))
ringi_ymbris = pygame.Surface((15,15))
ringiks = pygame.draw.circle(ringi_ymbris,(255,255,255),(int(15/2),int(15/2)),int(15/2))
ring = ringi_ymbris.convert()
ring.set_colorkey((0,0,0))

# some definitions
mangija_x, vastane_x = 10. , 620.
mangija_y, vastane_y = 215. , 215.
ring_x, ring_y = 307.5, 232.5
mangija_move, vastane_move = 0. , 0.
kiirus_x, kiirus_y, kiirus_circ = 250., 250., 250.
mangija_punktid, vastane_punktid = 0,0
#clock and font objects
kell = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

while True:
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                mangija_move = -ai_kiirus
            elif event.key == K_DOWN:
                mangija_move = ai_kiirus
        elif event.type == KEYUP:
            if event.key == K_UP:
                mangija_move = 0.
            elif event.key == K_DOWN:
                mangija_move = 0.
    
    punktid_1 = font.render(str(mangija_punktid), True,(255,255,255))
    punktid_2 = font.render(str(vastane_punktid), True,(255,255,255))

    aken.blit(taust,(0,0))
    frame = pygame.draw.rect(aken,(255,255,255),Rect((5,5),(630,470)),2)
    aken.blit(mangija,(mangija_x,mangija_y))
    aken.blit(vastane,(vastane_x,vastane_y))
    aken.blit(ring,(ring_x,ring_y))
    aken.blit(punktid_1,(250.,10.))
    aken.blit(punktid_2,(380.,10.))

    mangija_y += mangija_move
    
    aega_lainud = kell.tick(30)
    aeg = aega_lainud / 1000.0 #aeg sekundites
    
    ring_x += kiirus_x * aeg
    ring_y += kiirus_y * aeg
    ai_kiirus = kiirus_circ * aeg
#AI of the computer.
    if ring_x >= 305.:
        if not vastane_y == ring_y + 7.5:
            if vastane_y < ring_y + 7.5:
                vastane_y += ai_kiirus
            if  vastane_y > ring_y - 42.5:
                vastane_y -= ai_kiirus
        else:
            vastane_y == ring_y + 7.5
    
    if mangija_y >= 420.: mangija_y = 420.
    elif mangija_y <= 10. : mangija_y = 10.
    if vastane_y >= 420.: vastane_y = 420.
    elif vastane_y <= 10.: vastane_y = 10.
#since i don't know anything about collision, ball hitting bars goes like this.
    if ring_x <= mangija_x + 10.:
        if ring_y >= mangija_y - 7.5 and ring_y <= mangija_y + 42.5:
            ring_x = 20.
            kiirus_x = -kiirus_x
    if ring_x >= vastane_x - 15.:
        if ring_y >= vastane_y - 7.5 and ring_y <= vastane_y + 42.5:
            ring_x = 605.
            kiirus_x = -kiirus_x
    if ring_x < 5.:
        vastane_punktid += 1
        ring_x, ring_y = 320., 232.5
        mangija_y,bar_2_y = 215., 215.
    elif ring_x > 620.:
        mangija_punktid += 1
        ring_x, ring_y = 307.5, 232.5
        mangija_y, vastane_y = 215., 215.
    if ring_y <= 10.:
        kiirus_y = -kiirus_y
        ring_y = 10.
    elif ring_y >= 457.5:
        kiirus_y = -kiirus_y
        ring_y = 457.5

    pygame.display.update()
