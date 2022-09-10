import pygame,sys
pygame.init()
from pygame.locals import *
screen=pygame.display.set_mode((800,700),pygame.RESIZABLE)
pygame.display.set_caption("Pearl.exe")
clock=pygame.time.Clock()
fps=clock.get_fps()
pearl=pygame.image.load("pearl.png")
button=pygame.image.load("button.png")
buttonres=pygame.transform.scale(button,(370,100))
buttonres1=pygame.transform.scale(button,(450,100))
buttongame=pygame.Rect(200,150,370,100)
localbutton=pygame.Rect(200,300,370,100)
buttonswitch=pygame.Rect(170,450,450,100)
background=pygame.transform.scale(pygame.image.load("minecraft.png"),(2000,1000))
map=[1,1,1,1,1,1,1,1,1,1,1,1]
ul=pygame.Rect(275,125,55,55)
um=pygame.Rect(375,125,55,55)
ur=pygame.Rect(475,125,55,55)
ml=pygame.Rect(225,225,55,55)
mm1=pygame.Rect(325,225,55,55)
mm2=pygame.Rect(425,225,55,55)
mr=pygame.Rect(525,225,55,55)
dl=pygame.Rect(175,325,55,55)
dm1=pygame.Rect(275,325,55,55)
dm2=pygame.Rect(375,325,55,55)
dm3=pygame.Rect(475,325,55,55)
dr=pygame.Rect(575,325,55,55)
font=pygame.font.SysFont(None,100)
player1turn=True
player2turn=False

def draw_text(text,font,color,surface,x,y):
    textobj=font.render(text,1,color)
    textrect=textobj.get_rect()
    textrect.topleft=(x,y)
    screen.blit(textobj,textrect)
def game():
    global map,player1turn,player2turn,map
    turn=True
    click1=True
    click2=True
    click3=True
    run_game=True
    while run_game:
        clock.tick(60)
        mx,my=pygame.mouse.get_pos()
        click=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    run_game=False
                    map=[1,1,1,1,1,1,1,1,1,1,1,1]
                    menu()
            if event.type== MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        screen.fill((30,30,30))
        screen.blit(background,(0,0))
        if map[0]==1:
            pygame.draw.rect(screen,(255,255,255),ul)
            screen.blit(pearl,(250,100))
        if map[1]==1:
            pygame.draw.rect(screen,(255,255,255),um)
            screen.blit(pearl,(350,100))
        if map[2]==1:
            pygame.draw.rect(screen,(255,255,255),ur)
            screen.blit(pearl,(450,100))
        if map[3]==1:
            pygame.draw.rect(screen,(255,255,255),ml)
            screen.blit(pearl,(200,200))
        if map[4]==1:
            pygame.draw.rect(screen,(255,255,255),mm1)
            screen.blit(pearl,(300,200))
        if map[5]==1:
            pygame.draw.rect(screen,(255,255,255),mm2)
            screen.blit(pearl,(400,200))
        if map[6]==1:
            pygame.draw.rect(screen,(255,255,255),mr)
            screen.blit(pearl,(500,200))
        if map[7]==1:
            pygame.draw.rect(screen,(255,255,255),dl)
            screen.blit(pearl,(150,300))
        if map[8]==1:
            pygame.draw.rect(screen,(255,255,255),dm1)
            screen.blit(pearl,(250,300))
        if map[9]==1:
            pygame.draw.rect(screen,(255,255,255),dm2)
            screen.blit(pearl,(350,300))
        if map[10]==1:
            pygame.draw.rect(screen,(255,255,255),dm3)
            screen.blit(pearl,(450,300))
        if map[11]==1:
            pygame.draw.rect(screen,(255,255,255),dr)
            screen.blit(pearl,(550,300))
        if(click1==True):
            if ul.collidepoint((mx,my)):
                if click==True:
                    map[0]=0
                    click=False
                    click2=False
                    click3=False
            if um.collidepoint((mx,my)):
                if click==True:
                    map[1]=0
                    click=False
                    click2=False
                    click3=False
            if ur.collidepoint((mx,my)):
                if click==True:
                    map[2]=0
                    click=False
                    click2=False
                    click3=False
        if(click2==True):
            if ml.collidepoint((mx,my)):
                if click==True:
                    map[3]=0
                    click=False
                    click1=False
                    click3=False
            if mm1.collidepoint((mx,my)):
                if click==True:
                    map[4]=0
                    click=False
                    click1=False
                    click3=False
            if mm2.collidepoint((mx,my)):
                if click==True:
                    map[5]=0
                    click=False
                    click1=False
                    click3=False
            if mr.collidepoint((mx,my)):
                if click==True:
                    map[6]=0
                    click=False
                    click1=False
                    click3=False
        if(click3==True):
            if dl.collidepoint((mx,my)):
                if click==True:
                    map[7]=0
                    click=False
                    click1=False
                    click2=False
            if dm1.collidepoint((mx,my)):
                if click==True:
                    map[8]=0
                    click=False
                    click1=False
                    click2=False
            if dm2.collidepoint((mx,my)):
                if click==True:
                    map[9]=0
                    click=False
                    click1=False
                    click2=False
            if dm3.collidepoint((mx,my)):
                if click==True:
                    map[10]=0
                    click=False
                    click1=False
                    click2=False
            if dr.collidepoint((mx,my)):
                if click==True:
                    map[11]=0
                    click=False
                    click1=False
                    click2=False
        if (map[0]+map[1]+map[2]+map[3]+map[4]+map[5]+map[6]+map[7]+map[8]+map[9]+map[10]+map[11]==1):
            draw_text("you win",font,(60,60,60),screen,50,10)
            click1=False
            click2=False
            click3=False
        pygame.draw.rect(screen,(255,255,255),buttonswitch)
        screen.blit(buttonres1,(170,450))
        draw_text("I have played",font,(60,60,60),screen,170,465)
        if player1turn==True:
            draw_text("Player 1 turn",font,(60,60,60),screen,330,10)
        if player2turn==True:
            draw_text("Player 2 turn",font,(60,60,60),screen,330,10)
        if buttonswitch.collidepoint((mx,my)):
            if click==True:
                click1=True
                click2=True
                click3=True
                if player1turn==True:
                    player1turn=False
                    player2turn=True
                elif player2turn==True:
                    player1turn=True
                    player2turn=False
                
        pygame.display.update()

def fetchmenu():
    global screen
    run=True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type== MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    run=False
                    menu()
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)

        screen.fill((30,30,30))
        
        pygame.display.update()



def menu():
    global screen
    run=True
    while run:
        clock.tick(60)
        mx,my=pygame.mouse.get_pos()
        click=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type== MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
            if event.type==VIDEORESIZE:
                screen=pygame.display.set_mode((event.w,event.h),pygame.RESIZABLE)
        screen.fill((30,30,30))
        screen.blit(background,(0,0))
        draw_text("Pearl Game",font,(60,60,60),screen,200,20)
        pygame.draw.rect(screen,(255,255,255),buttongame)
        pygame.draw.rect(screen,(255,255,255),localbutton)
        screen.blit(buttonres,(200,150))
        draw_text("Play multi",font,(60,60,60),screen,210,165)
        screen.blit(buttonres,(200,300))
        draw_text("Play Local",font,(60,60,60),screen,210,315)
        if buttongame.collidepoint((mx,my)):
            if click==True:
                run=False
                game()
                print("pressed")
        if localbutton.collidepoint((mx,my)):
            if click==True:
                run=False
                fetchmenu()
        pygame.display.update()
menu()

