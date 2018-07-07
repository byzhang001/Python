import  sys,random,math,pygame
from pygame.locals import *

#main program begins
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Orbit Demo")

#LOAD BITMAPS
space=pygame.image.load("space.png").convert()
planet=pygame.image.load("planet2.png").convert_alpha()



ship=pygame.image.load("freelance.png").convert_alpha()
width,height=ship.get_size()
ship=pygame.transform.scale(ship,(width//2,height//2))

ship2=pygame.image.load("freelance.png").convert_alpha()
ship2=pygame.transform.smoothscale(ship,(width//2,height//2))


#repeating loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        #draw background
        screen.blit(space,(0,0))
        screen.blit(ship,(50,50))
        screen.blit(ship2,(50,150))
        screen.blit(planet,(400-width/2,300-height/2))

        pygame.display.update()
