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
font=pygame.font.Font("freesansbold.ttf",32)
textX=10
textY=10

over_f=pygame.font.Font("freesansbold.ttf",64)

def s_s(x,y):
    score=font.render("Score"+str(s_v),True,(255,255,255))
    screen.blit(score,(x,y))

def g_o_t():
    over_t=over_f.render("Game Over",True,(255,255,255))
    screen.blit(over_t,(200,500))

def pl(x,y):
    screen.blit(pImg,(x,y))

def en(x,y):
    screen.blit(eImg,(x,y))

def f_b(x,y):
    global b_s
    b_s="fire"
    screen.blit(bImg,(x+16,y+10))

def isCollid(enemyX,enemyY,bulletX,bulletY):
    dis=math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
    return dis<col_dis

running=True

while running:
    screen.fill((0,0,0))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                pXc-=5
            if event.key==pygame.K_RIGHT:
                pXc+=5
            if event.key==pygame.K_SPACE and b_s=="ready":
                bX=pX
                f_b(bX,bY)
        
        if event.type==pygame.KEYUP and event.key in (pygame.K_LEFT,pygame.K_RIGHT):
            pXc=0
        
        pX+=pXc
        pX=max(0,min(pX,s_w-64))

        for i in range(n_of_e):
            if eY[i]>340:
                for j in range(n_of_e):
                    eY[j]=2000
                g_o_t()
                break

            eX[i]+=eXc[i]
            if eX[i]<=0 or eX>=s_w-64:
                eXc[i]*=-1
                eY[i]+=eYc[i]

            if isCollid(eX[i],eY[i],bX,bY):
                bY=p_s_y
                b_s="ready"
                s_v+=1
                eX[i]=random.randint(0,s_w-64)
                eY[i]=random.randint(e_s_min_y,e_s_max_y)
            
            en(eX[i],eY[i])

            if bY<=0:
                bY=p_s_y
                b_s="ready"
            elif b_s=="fire":
                f_b(bX,bY)
                s_s(textX,textY)
                pygame.display.update()