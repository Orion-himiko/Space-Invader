import math
import random
import pygame

s_w=800
s_h=500
p_s_x=370
p_s_y=380
e_s_min_y=50
e_s_max_y=150
e_s_x=4
e_s_y=40
b_s_y=10
col_dis=27

pygame.init()

screen=pygame.display.set_mode((s_w,s_h))
bg=pygame.image.load('bg.jpg')

pygame.display.set_caption("Space Invader")

pImg=pygame.image.load('pl.png')
pX=p_s_x
pY=p_s_y
pXc=0

eImg=[]
eX=[]
eY=[]
eXc=[]
eYc=[]
n_of_e=6

for i in range(n_of_e):
    eImg.append(pygame.image.load('en.png'))
    eX.append(random.randint(0,s_w-64))
    eY.append(random.randint(e_s_min_y,e_s_max_y))
    eXc.append(e_s_x)
    eYc.append(e_s_y)

bImg=pygame.image.load('bl.png')
bX=0
bY=p_s_y
bXc=0
bYc=b_s_y
b_s="ready"

s_v=0
