import pygame,sys
from pygame.locals import *
import os
import time
import socketio
import threading

sio=socketio.Client()

pygame.init()

screen=pygame.display.set_mode((800,700),pygame.RESIZABLE)

pygame.display.set_caption("Pearl.exe")

background=pygame.transform.scale(pygame.image.load("minecraft.png"),(2000,1000))

clock=pygame.time.Clock()

fps=clock.get_fps()

user_text = ''
font = pygame.font.Font(None, 100)
button=pygame.image.load("button.png")
buttonres=pygame.transform.scale(button,(370,100))
runwait=True
rungame=True
nextturne=True
t=0
iswin=True
runplayagain=False
once=True
once1=True
once2=True


def draw_text(text,font,color,x,y):
    textobj=font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    screen.blit(textobj,textrect)

def username():
    global screen,user_text
    run=True
    input_rect = pygame.Rect(100, 250, 140, 100)
    active = False
    color_active = (60,60,60)
    color_passive = (50,50,50)
    color = color_passive
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(1)
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False
    
            if event.type == pygame.KEYDOWN:
    
                if event.key == pygame.K_BACKSPACE:
    
                    user_text = user_text[:-1]
    
                else:
                    user_text += event.unicode
                if event.key== pygame.K_RETURN:
                    user_text = user_text[:-1]
                    run=False
        
        screen.fill((30,30,30))
        screen.blit(background,(0,0))
        draw_text("TYPE YOUR NAME",font,(50,50,50),100,20)
        if active:
            color = color_active
        else:
            color = color_passive
            
        pygame.draw.rect(screen, color, input_rect)
    
        text_surface = font.render(user_text, True, (100, 100, 100))

        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        input_rect.w = max(600, text_surface.get_width()+10)
        
        pygame.display.update()


def menu():
    global screen
    run=True
    click=False
    createbutton=pygame.Rect(200,150,370,100)
    fetchbutton=pygame.Rect(200,300,370,100)
    exitbutton=pygame.Rect(200,450,370,100)
    while run:
        clock.tick(60)
        click=False
        mx,my=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run=False
                sio.disconnect()
                os._exit(1)
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
            if event.type== MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        
        screen.fill((30,30,30))
        screen.blit(background,(0,0))
        draw_text("Pearl GUI Client",font,(100,100,100),130,20)
        pygame.draw.rect(screen,(255,255,255),createbutton)
        screen.blit(buttonres,(200,150))
        draw_text("Play",font,(60,60,60),300,160)
        pygame.draw.rect(screen,(255,255,255),fetchbutton)
        screen.blit(buttonres,(200,300))
        draw_text("Fetch",font,(60,60,60),300,310)
        pygame.draw.rect(screen,(255,255,255),exitbutton)
        screen.blit(buttonres,(200,450))
        draw_text("EXIT",font,(60,60,60),300,470)
        if createbutton.collidepoint((mx,my)):
            if click==True:
                run=False
                sio.emit('creategame')
        if fetchbutton.collidepoint((mx,my)):
            if click==True:
                run=False
                sio.emit('fetchgames')
        if exitbutton.collidepoint((mx,my)):
            if click==True:
                sio.disconnect()
                os._exit(1)
        draw_text(f'HI {user_text}',font,(100,100,100),250,570)

        
        pygame.display.update()

def waiting():
    global screen,runwait
    runwait=True
    while runwait:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os._exit(1)
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
        screen.fill((30,30,30))
        screen.blit(background,(0,0))
        draw_text("Waiting FOR PLAYER",font,(150,150,150),50,100)
        draw_text("TO JOIN",font,(150,150,150),250,200)
        pygame.display.update()
    
def draw_game(gameobj):
    global screen,rungame,t,nextturne
    gameplay=gameobj["game"]["gameplay"]
    player1=gameobj["game"]["player1"]
    player2=gameobj["game"]["player2"]
    pearl=pygame.image.load("pearl.png")
    click1=True
    click2=True
    click3=True
    row=0
    numpearls=0
    draw=True
    rungame=False
    time.sleep(0.3)
    rungame=True
    donebutton=pygame.Rect(400,50,300,100)
    ul=pygame.Rect(175,225,55,55)
    um1=pygame.Rect(275,225,55,55)
    um2=pygame.Rect(375,225,55,55)
    um3=pygame.Rect(475,225,55,55)
    ur=pygame.Rect(575,225,55,55)
    ml=pygame.Rect(225,325,55,55)
    mm1=pygame.Rect(325,325,55,55)
    mm2=pygame.Rect(425,325,55,55)
    mr=pygame.Rect(525,325,55,55)
    dl=pygame.Rect(275,425,55,55)
    dm=pygame.Rect(375,425,55,55)
    dr=pygame.Rect(475,425,55,55)
    delul=False
    delum1=False
    delum2=False
    delum3=False
    delur=False
    delml=False
    delmm1=False
    delmm2=False
    delmr=False
    deldl=False
    deldm=False
    deldr=False
    global user_text
    while rungame:
        clock.tick(60)
        mx,my=pygame.mouse.get_pos()
        click=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sio.disconnect()
                os._exit(1)
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
            if event.type== MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        screen.fill((30,30,30))
        screen.blit(background,(0,0))
        draw_text(f'{player1["username"]}',font,(150,150,150),50,50)
        draw_text(f':{player1["score"]}',font,(150,150,150),300,50)
        draw_text(f'{player2["username"]}',font,(150,150,150),50,100)
        draw_text(f':{player2["score"]}',font,(150,150,150),300,100)
        pygame.draw.rect(screen,(255,255,255),donebutton)
        screen.blit(buttonres,(400,50))
        draw_text("Done",font,(150,150,150),430,50)
        if draw==True:
            if gameplay[0][0]==1:
                if not delul:
                    pygame.draw.rect(screen,(255,255,255),ul)
                    screen.blit(pearl,(150,200))
            if gameplay[0][1]==1:
                if not delum1:
                    pygame.draw.rect(screen,(255,255,255),um1)
                    screen.blit(pearl,(250,200))
            if gameplay[0][2]==1:
                if not delum2:
                    pygame.draw.rect(screen,(255,255,255),um2)
                    screen.blit(pearl,(350,200))
            if gameplay[0][3]==1:
                if not delum3:
                    pygame.draw.rect(screen,(255,255,255),um3)
                    screen.blit(pearl,(450,200))
            if gameplay[0][4]==1:
                if not delur:
                    pygame.draw.rect(screen,(255,255,255),ur)
                    screen.blit(pearl,(550,200))
            if gameplay[1][0]==1:
                if not delml:
                    pygame.draw.rect(screen,(255,255,255),ml)
                    screen.blit(pearl,(200,300))
            if gameplay[1][1]==1:
                if not delmm1:
                    pygame.draw.rect(screen,(255,255,255),mm1)
                    screen.blit(pearl,(300,300))
            if gameplay[1][2]==1:
                if not delmm2:
                    pygame.draw.rect(screen,(255,255,255),mm2)
                    screen.blit(pearl,(400,300))
            if gameplay[1][3]==1:
                if not delmr:
                    pygame.draw.rect(screen,(255,255,255),mr)
                    screen.blit(pearl,(500,300))
            if gameplay[2][0]==1:
                if not deldl:
                    pygame.draw.rect(screen,(255,255,255),dl)
                    screen.blit(pearl,(250,400))
            if gameplay[2][1]==1:
                if not deldm:
                    pygame.draw.rect(screen,(255,255,255),dm)
                    screen.blit(pearl,(350,400))
            if gameplay[2][2]==1:
                if not deldr:
                    pygame.draw.rect(screen,(255,255,255),dr)
                    screen.blit(pearl,(450,400))

        
        if gameobj["turn"]==True:
            draw_text(f'Your Turn {user_text}',font,(150,150,150),100,600)
            if(click1==True):
                if ul.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click2=False
                        click3=False
                        delul=True
                        row=1
                        numpearls=numpearls+1
                if um1.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click2=False
                        click3=False
                        delum1=True
                        row=1
                        numpearls=numpearls+1
                if um2.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click2=False
                        click3=False
                        delum2=True
                        row=1
                        numpearls=numpearls+1
                if um3.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click2=False
                        click3=False
                        delum3=True
                        row=1
                        numpearls=numpearls+1
                if ur.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click2=False
                        click3=False
                        delur=True
                        row=1
                        numpearls=numpearls+1
            if click2==True:
                if ml.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click1=False
                        click3=False
                        delml=True
                        row=2
                        numpearls=numpearls+1
                if mm1.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click1=False
                        click3=False
                        delmm1=True
                        row=2
                        numpearls=numpearls+1
                if mm2.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click1=False
                        click3=False
                        delmm2=True
                        row=2
                        numpearls=numpearls+1
                if mr.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click1=False
                        click3=False
                        delmr=True
                        row=2
                        numpearls=numpearls+1
            if click3==True:
                if dl.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click1=False
                        click2=False
                        deldl=True
                        row=3
                        numpearls=numpearls+1
                if dm.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click1=False
                        click2=False
                        deldm=True
                        row=3
                        numpearls=numpearls+1
                if dr.collidepoint((mx,my)):
                    if click==True:
                        click=False
                        click1=False
                        click2=False
                        deldr=True
                        row=3
                        numpearls=numpearls+1


        else:
            draw_text(f"{gameobj['opponent']}'s Turn",font,(150,150,150),100,600)

        if gameobj["turn"]==False:
            nextturne=True
        if donebutton.collidepoint((mx,my)):
            if click==True:
                if row==0 or numpearls==0:
                    click=False
                time.sleep(0.3)
                nextturne=True
                sio.emit('removepearls', {"row":row,"pearls":numpearls})
                click=False

        pygame.display.update()

def playagain():
    global iswin,screen,runplayagain
    runplayagain=True
    while runplayagain:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sio.disconnect()
                os._exit(1)
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_y:
                    runplayagain=False
                    sio.emit('playagain')  
                if event.key==pygame.K_n:
                    runplayagain=False
                    sio.emit('noplayagain')
        screen.fill((30,30,30))
        screen.blit(background,(0,0))
        draw_text("Pearl GUI Client",font,(150,150,150),100,50)
        if iswin==True:
            draw_text("You WIN!",font,(150,150,150),100,150)
        else:
            draw_text("YOU LOSE!:(",font,(150,150,150),100,150)
        draw_text("Do You Want To",font,(150,150,150),100,250)
        draw_text("Play Again? Press",font,(150,150,150),100,350)
        draw_text("Y or N",font,(150,150,150),100,450)

        pygame.display.update()

def fetch(freegames):
    global screen
    run=True
    w1=100

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sio.disconnect()
                os._exit(1)
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
        screen.fill((30,30,30))
        screen.blit(background,(0,0))
        for i in range(0,len(freegames)):
            draw_text(f'{i+1}  {freegames[i]["creator"]}',font,(150,150,150),100,w1)
        pygame.display.update()    


menuthread=threading.Thread(target=menu)
waitingthread=threading.Thread(target=waiting)
gamethread=threading.Thread(target=draw_game,args=(None))
againthread=threading.Thread(target=playagain)

username()

@sio.event
def connect():
    print(sio.sid)
    print('Connection established')
    menuthread.start()

@sio.event
def gamecreated():
    global once
    print("Game created")
    print("Waiting for Player to Join")
    if once:
        waitingthread.start()
        once=False
    else:
        waiting()

@sio.event
def loadinggame(loader):
    global runwait
    print("Starting Game with",loader["opponent"])
    runwait=False
    draw_game(loader)

@sio.event
def nextturn(gameobj):
    global nextturne
    if nextturne:
        draw_game(gameobj)
        nextturne=False

@sio.event
def winner():
    global rungame,iswin
    rungame=False
    iswin=True
    playagain()

@sio.event
def looser():
    global rungame,iswin
    rungame=False
    iswin=False
    playagain()

@sio.event
def tomainmenu():
    menu()

@sio.event
def opponentleft(opponentname):
    global rungame,runplayagain
    rungame=False
    runplayagain=False
    print(f"{opponentname} left the game.")
    menu()

@sio.event
def showgames(freegames):
    print("Free Games")
    # print(freegames)
    if len(freegames)>0:
        fetch(freegames)
    else:
        menu()
    

sio.connect('http://localhost:5000/')
sio.emit('Connection', user_text)
