import pygame
import time
import random
import math
from pygame import mixer

pygame.init()

score=0
font=pygame.font.SysFont(None,38)
textX=10
textY=10
def show(x,y):
    scorevalue=font.render("your score is: "+ str(score), True, (255,255,255))
    screen.blit(scorevalue,(x,y))
#music
mixer.music.load('background.wav')
mixer.music.play(-1)

screen = pygame.display.set_mode((1000, 800))
#title
pygame.display.set_caption("Lou Wagner")
icon = pygame.image.load('icon.jpeg')
pygame.display.set_icon(icon)
image= pygame.image.load('lou.jpeg')
LouX=450
LouY=700

newX=0
newY=0
#meat
meatpic= pygame.image.load('meat.png')
meatX=random.randint(10,900)
meatY=random.randint(10,300)
meatNewX=0.3
#diary
Diarypic= pygame.image.load('Diary.png')
DiaryX=random.randint(10,900)
DiaryY=random.randint(10,300)
DiaryNewX=0.3
#egg
eggpic= pygame.image.load('egg.png')
eggX=random.randint(10,900)
eggY=random.randint(10,300)
eggNewX=0.3
#Backup
backuppic=[]
backupx=[]
backupy=[]
backupnew=1

backuppic.append(pygame.image.load('bee.png'))
backuppic.append(pygame.image.load('bird.png'))
backuppic.append(pygame.image.load('cow.png'))
backuppic.append(pygame.image.load('hen.png'))
backuppic.append(pygame.image.load('owl.png'))


for i in range(0,5):

    backupx.append(random.randint(10, 900))
    backupy.append(random.randint(1000, 5000))


#Background
Background=pygame.image.load('newyork.jpeg')
#9ertassa
kertassa=pygame.image.load('9ertassa.png')
kertassaY=LouY
kertassaX=0
kerrtassaNew=10
kertassastatu="hey"
def fire(x,y):
    global kertassastatu
    kertassastatu="ho"
    screen.blit(kertassa,(x+10,y-20))
def boom(x1,y1,x2,y2):
    boom=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    if boom<130:
        return True
    else:
        return False


def meat(X,Y):
    screen.blit(meatpic, (X,Y))
def Diary(X,Y):
    screen.blit(Diarypic, (X,Y))
def egg(X,Y):
    screen.blit(eggpic, (X,Y))

def backup(i,X,Y):
    if backupy[i]<1200 and backupy[i]>-100:
        screen.blit(backuppic[i], (backupx[i],backupy[i]))

def lou(LouX,LouY):
    screen.blit(image, (LouX,LouY))
font=pygame.font.SysFont(None, 90)
color=(255,255,255)
def msg(msg, color):
    text=font.render(msg, True, color)
    screen.blit(text,[150,350])
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                newX=-3
            if event.key==pygame.K_RIGHT:
                newX=3
            if event.key==pygame.K_UP:
                newY=-3
            if event.key==pygame.K_DOWN:
                newY=3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                newX=0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                newY=0
            if event.key==pygame.K_SPACE:
                if kertassastatu=="hey":
                    kertassaY=LouY
                    kertassaX=LouX
                    fire(kertassaX,kertassaY)
                    sound=mixer.Sound('laser.wav')
                    sound.play()

    LouX=LouX+newX
    if LouX<10 or LouX>922:
        LouX = LouX - newX
    LouY=LouY+newY
    if LouY<50 or LouY>700:
        LouY = LouY - newY

    screen.fill((0,0,0))
    screen.blit(Background,(0,-100))
    lou(LouX, LouY)
    Diary(DiaryX, DiaryY)
    egg(eggX,eggY)
    eggX+=eggNewX
    DiaryX = DiaryX + DiaryNewX
    if DiaryX <= 0:
        DiaryNewX = 0.8
        DiaryY = DiaryY + 70
    elif DiaryX >= 950:
        DiaryNewX = -0.8
        DiaryY = DiaryY + 250

    egg(eggX, eggY)
    eggX = eggX + eggNewX
    if eggX <= 0:
        eggNewX = 0.8
        eggY = eggY + 100
    elif eggX >= 950:
        eggNewX = -0.45
        eggY = eggY + 100

    meat(meatX,meatY)
    meatX=meatX+meatNewX
    if meatX<=0:
        meatNewX=0.25
        meatY=meatY+50
    elif meatX>=950:
        meatNewX=-0.25
        meatY = meatY + 180
    for i in range(0,5):
        backup(i,backupx[i], backupy[i])
        backupy[i] = backupy[i] - backupnew
        if backupy[i]<-5000:
            backupx[i]=random.randint(10, 900)
            backupy[i]=random.randint(0, 1000)




    if kertassastatu == "ho":
        fire(kertassaX,kertassaY)
        kertassaY=kertassaY-4
        if kertassaY<0:
            kertassaY=LouY
            kertassastatu="hey"
    collision=boom(meatX,meatY,kertassaX,kertassaY)
    collision2=boom(DiaryX,DiaryY,kertassaX,kertassaY)
    collision3 = boom(eggX, eggY, kertassaX, kertassaY)
    if collision and kertassastatu=="ho":
        expolision=mixer.Sound('explosion.wav')
        expolision.play()
        score+=1
        kertassaY = LouY
        kertassastatu = "hey"
        print("you did it! now your score is", score)
        meatX = random.randint(10, 900)
        meatY = random.randint(10, 300)
    for i in range(5):
        x=int(backupx[i])
        y=int(backupy[i])
        if boom(meatX,meatY,x,y):
            horse = mixer.Sound('horse.wav')
            horse.play()
            meatX = random.randint(10, 900)
            meatY = random.randint(10, 300)
            backupx[i]=random.randint(10, 900)
            backupy[i]=random.randint(-1000, 0)
        if boom(DiaryX, DiaryY, x, y):
            horse = mixer.Sound('horse.wav')
            horse.play()
            DiaryX = random.randint(10, 900)
            DiaryY = random.randint(10, 300)
            backupx[i] = random.randint(10, 900)
            backupy[i] = random.randint(-1000, 0)
        if boom(eggX, eggY, x, y):
            horse = mixer.Sound('horse.wav')
            horse.play()
            eggX = random.randint(10, 900)
            eggY = random.randint(10, 300)
            backupx[i] = random.randint(10, 900)
            backupy[i] = random.randint(-1000, 0)



    if collision2 and kertassastatu=="ho":
        expolision = mixer.Sound('explosion.wav')
        expolision.play()
        score += 2
        kertassaY = LouY
        kertassastatu = "hey"
        print("you did it! now your score is", score)
        DiaryX = random.randint(10, 900)
        DiaryY = random.randint(10, 300)
    if collision3 and kertassastatu=="ho":
        expolision = mixer.Sound('explosion.wav')
        expolision.play()
        score += 3
        kertassaY = LouY
        kertassastatu = "hey"
        print("you did it! now your score is", score)
        eggX = random.randint(10, 900)
        eggY = random.randint(10, 300)
    if eggY>800 or DiaryY>800 or meatY>800:
        msg("you suck, you ar out", color)
        pygame.display.update()
        time.sleep(3)
        show(250,200)
        pygame.display.update()
        time.sleep(4)
        pygame.quit()
        quit()

    show(textX,textY)


    pygame.display.update()

