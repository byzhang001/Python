import pygame,sys,time,random
from pygame.locals import *

def print_text(font,x,y,text,color=(255,255,255)):
    imgText=font.render(text,True,color)
    screen.blit(imgText,(x,y))
#main program begings
pygame.init()
screen=pygame.display.set_mode((600,500))
pygame.display.set_caption("Bomb Catching Game")
font1=pygame.font.Font(None,24)
pygame.mouse.set_visible(False)
white=255,255,255
red=220,50,50
yellow=230,230,50
black=0,0,0

lives=3
score=0
game_over=True
mouse_x=mouse_y=0
pos_x=300
pos_y=460
bomb_x=random.randint(0,500)
bomb_y=-50
vel_y=0.7

#repeating loop
while True:
    for event in pygame.event.get():
        if event.type ==QUIT:
            sys.exit()
        elif event.type==MOUSEMOTION:
            mouse_x,mouse_y=event.pos
            move_x,move_y=event.rel
        elif event.type==MOUSEBUTTONUP:
            if game_over:
                game_over=False
                lives=3
                score=0
    keys=pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()

    screen.fill((0,0,100))
    if game_over:
        print_text(font1,100,200,"<CLICK TO REPLAY")
    else:
        #move the bomb
        bomb_y+=vel_y

        #has the player missed teh bomb?
        if bomb_y>500:
            bomb_x=random.randint(0,500)
