background_1_image_filename='/home/wfy/Finger-guessing/1.jpg'
background_2_image_filename='/home/wfy/Finger-guessing/3.png'
background_4_image_filename='/home/wfy/Finger-guessing/4.jpg'
background_5_image_filename='/home/wfy/Finger-guessing/5.jpg'
background_6_image_filename='/home/wfy/Finger-guessing/6.jpg'
mouse_image_filename='/home/wfy/Finger-guessing/egg1.png'

import pygame
from pygame.locals import *
from sys import exit
from random import *
pygame.init()
SCREEN_SIZE=(1200,600)
Fullscreen=False
screen=pygame.display.set_mode(SCREEN_SIZE,0,32)

pygame.display.set_caption("Finger-guessing Game")
background_1=pygame.image.load(background_1_image_filename).convert()
background_2=pygame.image.load(background_2_image_filename).convert()
background_3=pygame.image.load(background_2_image_filename).convert()
background_4=pygame.image.load(background_4_image_filename).convert()
background_5=pygame.image.load(background_5_image_filename).convert()
background_6=pygame.image.load(background_6_image_filename).convert()
mouse_cursor=pygame.image.load(mouse_image_filename).convert_alpha()


x,y=0,0
move_x,move_y=0,0
background=background_1
#clock
clock=pygame.time.Clock()
x_time=0.
x_time2=0
speed=250
x_pos=0
y_pos=0

i=-1
j=-1
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()


        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                move_x=-1
            elif event.key==K_RIGHT:
                move_x=1
            elif event.key==K_UP:
                move_y=-1
            elif event.key==K_DOWN:
                move_y=1
            elif event.key==K_f:
                Fullscreen=not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode(SCREEN_SIZE,FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
            elif event.key == K_s:
                background=background_2
        elif event.type==KEYUP:
            x+=move_x
            y+=move_y
            break
        if event.type==MOUSEMOTION:
           x, y = pygame.mouse.get_pos()
           x -= mouse_cursor.get_width() / 2
           y -= mouse_cursor.get_height() / 2

    pressed_mouse=pygame.mouse.get_pressed()
    if pressed_mouse[0]:
        x_pos,y_pos=pygame.mouse.get_pos()
        if (x_pos>465)and(x_pos<725)and(y_pos>235)and(y_pos<320):
            background=background_2

    screen.blit(background,(0,0))

    if (background==background_2):
        rc_red=(252,118,119)
        rc_green=(161,191,193)
        rp1=[(350,140),(350,280),(350,420)]
        rp2=[(850,140),(850,280),(850,420)]
        rr =60
        if x_time<300:
            pygame.draw.circle(screen, rc_red, rp2[1], rr)
            pygame.draw.circle(screen, rc_red, rp2[2], rr)
            x_time+=1
        elif (x_time<600)and(x_time>=300):
            pygame.draw.circle(screen, rc_red, rp2[0], rr)
            pygame.draw.circle(screen, rc_red, rp2[2], rr)
            x_time+=1
        elif (x_time < 900)and(x_time>=600):
            pygame.draw.circle(screen, rc_red, rp2[0], rr)
            pygame.draw.circle(screen, rc_red, rp2[1], rr)
            x_time+=1
        else:
            x_time=0
        if pressed_mouse[0]:
            x_pos, y_pos = pygame.mouse.get_pos()
            if ((x_pos > 300) and (x_pos < 400) and (y_pos > 90) and (y_pos < 210))\
                    or((x_pos > 300) and (x_pos < 400) and (y_pos > 230) and (y_pos < 330)) \
                    or ((x_pos > 300) and (x_pos < 400) and (y_pos > 370) and (y_pos < 470)):
                background = background_3
                i=randint(0,2)
                j=randint(0,2)
                while(i==j):
                    i=randint(0,2)
    if(background==background_3):
        if ((x_pos > 300) and (x_pos < 400) and (y_pos > 230) and (y_pos < 330)):
            if x_time2<500:
                pygame.draw.circle(screen, rc_green, rp1[0], rr)
                pygame.draw.circle(screen, rc_green, rp1[2], rr)
                pygame.draw.circle(screen, rc_red, rp2[i], rr)
                pygame.draw.circle(screen, rc_red, rp2[j], rr)
                x_time2 += 1
            else:
                if i+j==3:
                    background=background_5
                elif i+j==2:
                    background=background_6
                elif i+j==1:
                    background=background_4
                x_time2=0
        if ((x_pos > 300) and (x_pos < 400) and (y_pos > 90) and (y_pos < 210)):
            if x_time2<500:
                pygame.draw.circle(screen, rc_green, rp1[1], rr)
                pygame.draw.circle(screen, rc_green, rp1[2], rr)
                pygame.draw.circle(screen, rc_red, rp2[i], rr)
                pygame.draw.circle(screen, rc_red, rp2[j], rr)
                x_time2 += 1
            else:
                if i + j == 3:
                    background = background_6
                elif i + j == 2:
                    background = background_4
                elif i + j == 1:
                    background = background_5
                x_time2 = 0

        if ((x_pos > 300) and (x_pos < 400) and (y_pos > 370) and (y_pos < 470)):
            if x_time2<500:
                pygame.draw.circle(screen, rc_green, rp1[0], rr)
                pygame.draw.circle(screen, rc_green, rp1[1], rr)
                pygame.draw.circle(screen, rc_red, rp2[i], rr)
                pygame.draw.circle(screen, rc_red, rp2[j], rr)
                x_time2 += 1
            else:
                if (i+j)==3:
                    background=background_4
                elif (i+j)==2:
                    background=background_5
                elif (i+j)==1:
                    background=background_6
                x_time2=0
    if pressed_mouse[2]:
        background=background_2
    screen.blit(mouse_cursor, (x, y))
    pygame.display.update()