import pygame
import random
from pygame import mixer


pygame.init()

#SCREEN
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Pong")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
font=pygame.font.Font("freesansbold.ttf",20)

running=True
player1score=0
player2score=0

playerw=25
playerh=100
pdy=0
#PLAYER 1
playerx=25
playery=300

#PLAYER 2
player2x=750
player2y=300
p2dy=0
#BALL
bh=25
bw=25
ballx=400
bally=300
bdx=-0.25
bdy=bdx
#RUNNING LOOP
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_w:
                pdy=-0.5


            if event.key==pygame.K_s:
                pdy=0.5


            if event.key==pygame.K_UP:
                p2dy=-0.5


            if event.key==pygame.K_DOWN:
                p2dy=0.5

        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                pdy = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                p2dy = 0

    #after miss
    if ballx<10:
        player2score+=1
        ballx=400
        bally=random.randint(25,575)
        if random.randint(0,1)==0 :
            bdx=-0.25
        else:
            bdx=0.25

    if ballx>765:
        player1score+=1
        ballx=400
        bally=random.randint(25,575)
        if random.randint(0,1)==0 :
            bdx=-0.25
        else:
            bdx=0.25


    if bally>=575:
        bdy=-bdy

    if bally<=0:
        bdy=abs(bdy)

        # ball logic
    if (ballx >= player2x - playerw and player2y <= bally + bh and bally <= player2y + playerh):
        bdx = -abs(bdx)
        mixer.Sound("boing.mp3").play()
        bdx -= 0.01
        bdx -= 0.01

    if (ballx <= playerx + playerw and playery <= bally + bh and bally <= playery + playerh):
        bdx = abs(bdx)
        mixer.Sound("boing.mp3").play()
        bdx += 0.01
        bdx += 0.01

    #player collison logic
    if playery>=500:
        playery=500
    if playery<=0:
        playery=0
    if player2y>=500:
        player2y=500
    if player2y<=0:
        player2y=0



    ballx += bdx
    bally += bdy

    playery+=pdy
    player2y+=p2dy

    sc = font.render(f"player1:{player1score}           player2:{player2score}", True, (255, 255, 255))
    screen.blit(sc,(300,0))
    pygame.draw.rect(screen, (255, 255, 255), (playerx, playery, playerw, playerh))
    pygame.draw.rect(screen, (255, 255, 255), (player2x, player2y, playerw, playerh))
    pygame.draw.rect(screen, (255, 255, 255), (ballx, bally, bw, bh))
    pygame.display.update()
