import pygame, random, os
from pygame.locals import *
import numpy as np 
pygame.init()


board=np.array([[0]*10]*20)
win=pygame.display.set_mode((700,1000))
pygame.display.set_caption('Tetris')
icon=pygame.image.load(os.path.join('Assets','gfx','Icon.png'))
pygame.display.set_icon(icon)

Background=pygame.image.load(os.path.join('Assets','gfx','Background.png'))

Block0=pygame.image.load(os.path.join('Assets','gfx','Block0.png'))
Block1=pygame.image.load(os.path.join('Assets','gfx','Block1.png'))
Block2=pygame.image.load(os.path.join('Assets','gfx','Block2.png'))
Block3=pygame.image.load(os.path.join('Assets','gfx','Block3.png'))
Block4=pygame.image.load(os.path.join('Assets','gfx','Block4.png'))
Block5=pygame.image.load(os.path.join('Assets','gfx','Block5.png'))
Block6=pygame.image.load(os.path.join('Assets','gfx','Block6.png'))
Block7=pygame.image.load(os.path.join('Assets','gfx','Block7.png'))

music=pygame.mixer.music.load(os.path.join('Assets','sfx','Background_Music.mp3'))
single_sfx=pygame.mixer.Sound(os.path.join('Assets','sfx','Single.wav'))
double_sfx=pygame.mixer.Sound(os.path.join('Assets','sfx','Double.wav'))
triple_sfx=pygame.mixer.Sound(os.path.join('Assets','sfx','Triple.wav'))
tetris_sfx=pygame.mixer.Sound(os.path.join('Assets','sfx','Tetris.wav'))
move_sfx=pygame.mixer.Sound(os.path.join('Assets','sfx','Move.wav'))
rotate_sfx=pygame.mixer.Sound(os.path.join('Assets','sfx','Rotate.wav'))

pygame.mixer.music.set_volume(0.3)
rotate_sfx.set_volume(0.1)
double_sfx.set_volume(0.1)
single_sfx.set_volume(0.1)
triple_sfx.set_volume(0.1)
tetris_sfx.set_volume(0.1)
move_sfx.set_volume(0.1)


font=pygame.font.Font(os.path.join('Assets','gfx','Font.ttf'),38)
font2=pygame.font.Font(os.path.join('Assets','gfx','Font.ttf'),30)
font3=pygame.font.Font(os.path.join('Assets','gfx','Bold.ttf'),90)
font4=pygame.font.Font(os.path.join('Assets','gfx','Bold.ttf'),65)

ch=0
r=0
score=0


def display():
    title=font.render("T E T R I S",True,(92,229,193))
    title_rect=title.get_rect()
    title_rect.center=(350,45)
    text=''
    for i in str(score):
        text=text+' '+i
    score_text=font2.render("S C O R E -"+text,True,(230,93,93))
    score_rect=score_text.get_rect()
    score_rect.center=(350,970)
    win.blit(Background,(0,0))
    win.blit(score_text,score_rect)
    win.blit(title,title_rect)
    for i in range(0,20):
        for j in range(0,10):
            if board[i][j]<8 and board[i][j]!=0:
                board[i][j]=0
    
    for i in spawn_block:
        if board[i[0]][i[1]]<8:
            board[i[0]][i[1]]=ch

    for i in range(0,20):
        for j in range(0,10):
            if board[i][j]==0:
                win.blit(Block0,(j*40+150,i*40+100))
            elif board[i][j]==1 or board[i][j]==8:
                win.blit(Block1,(j*40+150,i*40+100))
            elif board[i][j]==2 or board[i][j]==9:
                win.blit(Block2,(j*40+150,i*40+100))
            elif board[i][j]==3 or board[i][j]==10:
                win.blit(Block3,(j*40+150,i*40+100))
            elif board[i][j]==4 or board[i][j]==11:
                win.blit(Block4,(j*40+150,i*40+100))
            elif board[i][j]==5 or board[i][j]==12:
                win.blit(Block5,(j*40+150,i*40+100))
            elif board[i][j]==6 or board[i][j]==13:
                win.blit(Block6,(j*40+150,i*40+100))
            elif board[i][j]==7 or board[i][j]==14:
                win.blit(Block7,(j*40+150,i*40+100))
            


def spawn():
    global spawn_block
    global ch
    global r
    flag=False

    r=0
    ch=random.randint(1,7)
    if ch==1:
        spawn_block=np.array([[1,5],[0,4],[0,5],[0,6]])
    elif ch==2:
        spawn_block=np.array([[1,4],[1,5],[0,4],[0,5]])
    elif ch==3:
        spawn_block=np.array([[1,5],[0,3],[1,4],[0,4]])
    elif ch==4:
        spawn_block=np.array([[0,3],[0,4],[0,5],[0,6]])
    elif ch==5:
        spawn_block=np.array([[1,4],[0,4],[0,5],[0,6]])
    elif ch==6:
        spawn_block=np.array([[0,3],[1,3],[1,4],[1,5]])
    elif ch==7:
        spawn_block=np.array([[1,4],[1,5],[0,5],[0,6]])

    for i in spawn_block:
        if board[i[0]][i[1]]>7:
            flag=True

    for i in spawn_block:
        if board[i[0]][i[1]]<8:
            board[i[0]][i[1]]=ch
    return flag


def iteration():
    flag=False
    global spawn_block
    #pygame.mixer.Sound.play(move_sfx)
    for i in spawn_block:
        if i[0]==19 or board[i[0]+1][i[1]]>7:
            flag=True
            break
    if not(flag):
        for i in range(0,len(spawn_block)):
            spawn_block[i][0]+=1
        for i in range(0,20):
            for j in range(0,10):
                if board[i][j]<=7:
                    board[i][j]=0
        for i in spawn_block:
            board[i[0]][i[1]]=ch
    else:
        for i in range(0,20):
            for j in range(0,10):
                if board[i][j]<8 and board[i][j]!=0:
                    board[i][j]+=7
    return flag

def move(dir):
    flag=True
    pygame.mixer.Sound.play(move_sfx)
    global spawn_block
    if dir>0:
        for i in spawn_block:
            if i[1]+1>9:
                flag=False
                break
            elif board[i[0]][i[1]+1]>7:
                flag=False
                break
        if flag:
            for i in range(0,len(spawn_block)):
                spawn_block[i][1]+=1
    else:
        for i in spawn_block:
            if i[1]-1<0:
                flag=False
                break
            elif board[i[0]][i[1]-1]>7:#test
                flag=False
                break
        if flag:
            for i in range(0,len(spawn_block)):
                spawn_block[i][1]-=1


def rotate():
    global ch
    flag=True
    global spawn_block
    y_shift=0
    x_shift=0

    pygame.mixer.Sound.play(rotate_sfx)
    if ch==1:
        m=spawn_block[2]
        if r%4==0:
            newSpawn=np.array([[m[0]-1,m[1]],[m[0],m[1]-1],[m[0],m[1]],[m[0]+1,m[1]]])
        if r%4==1:
            newSpawn=np.array([[m[0]-1,m[1]],[m[0],m[1]-1],[m[0],m[1]],[m[0],m[1]+1]])
        if r%4==2:
            newSpawn=np.array([[m[0]-1,m[1]],[m[0]+1,m[1]],[m[0],m[1]],[m[0],m[1]+1]])
        if r%4==3:
            newSpawn=np.array([[m[0],m[1]-1],[m[0],m[1]+1],[m[0],m[1]],[m[0]+1,m[1]]])
    
    elif ch==2:
        newSpawn=spawn_block
    
    elif ch==3:
        m=spawn_block[2]
        if r%4==0:
            newSpawn=np.array([[m[0]-1,m[1]+1],[m[0],m[1]+1],[m[0],m[1]],[m[0]+1,m[1]]])
        if r%4==1:
            newSpawn=np.array([[m[0],m[1]-1],[m[0]+1,m[1]],[m[0],m[1]],[m[0]+1,m[1]+1]])
        if r%4==2:
            newSpawn=np.array([[m[0]-1,m[1]],[m[0],m[1]-1],[m[0],m[1]],[m[0]+1,m[1]-1]])
        if r%4==3:
            newSpawn=np.array([[m[0]-1,m[1]-1],[m[0]-1,m[1]],[m[0],m[1]],[m[0],m[1]+1]])
    elif ch==4:
        m=spawn_block[2]
        if r%4==0:
            newSpawn=np.array([[m[0]-2,m[1]],[m[0]-1,m[1]],[m[0],m[1]],[m[0]+1,m[1]]])
        if r%4==1:
            newSpawn=np.array([[m[0],m[1]-1],[m[0],m[1]+1],[m[0],m[1]],[m[0],m[1]+2]])
        if r%4==2:
            newSpawn=np.array([[m[0]-1,m[1]],[m[0]+1,m[1]],[m[0],m[1]],[m[0]+2,m[1]]])
        if r%4==3:
            newSpawn=np.array([[m[0],m[1]-2],[m[0],m[1]-1],[m[0],m[1]],[m[0],m[1]+1]])
    elif ch==5:
        m=spawn_block[2]
        if r%4==0:
            newSpawn=np.array([[m[0]-1,m[1]-1],[m[0]-1,m[1]],[m[0],m[1]],[m[0]+1,m[1]]])
        if r%4==1:
            newSpawn=np.array([[m[0]-1,m[1]+1],[m[0],m[1]-1],[m[0],m[1]],[m[0],m[1]+1]])
        if r%4==2:
            newSpawn=np.array([[m[0]+1,m[1]+1],[m[0]+1,m[1]],[m[0],m[1]],[m[0]-1,m[1]]])
        if r%4==3:
            newSpawn=np.array([[m[0]+1,m[1]-1],[m[0],m[1]-1],[m[0],m[1]],[m[0],m[1]+1]])
    elif ch==6:
        m=spawn_block[2]
        if r%4==0:
            newSpawn=np.array([[m[0]-1,m[1]],[m[0]-1,m[1]+1],[m[0],m[1]],[m[0]+1,m[1]]])
        if r%4==1:
            newSpawn=np.array([[m[0],m[1]-1],[m[0],m[1]+1],[m[0],m[1]],[m[0]+1,m[1]+1]])
        if r%4==2:
            newSpawn=np.array([[m[0]-1,m[1]],[m[0]+1,m[1]],[m[0],m[1]],[m[0]+1,m[1]-1]])
        if r%4==3:
            newSpawn=np.array([[m[0],m[1]-1],[m[0],m[1]+1],[m[0],m[1]],[m[0]-1,m[1]-1]])
    elif ch==7:
        m=spawn_block[2]
        if r%4==0:
            newSpawn=np.array([[m[0]+1,m[1]],[m[0],m[1]-1],[m[0],m[1]],[m[0]-1,m[1]-1]])
        if r%4==1:
            newSpawn=np.array([[m[0]-1,m[1]],[m[0],m[1]-1],[m[0],m[1]],[m[0]-1,m[1]+1]])
        if r%4==2:
            newSpawn=np.array([[m[0]-1,m[1]],[m[0],m[1]+1],[m[0],m[1]],[m[0]+1,m[1]+1]])
        if r%4==3:
            newSpawn=np.array([[m[0]+1,m[1]],[m[0],m[1]+1],[m[0],m[1]],[m[0]+1,m[1]-1]])
            
    for i in newSpawn:
        if i[1]>9:
            y_shift-=1
        elif i[1]<0:
            y_shift+=1
        if i[0]<0:
            x_shift+=1
        if i[0]>19:
            x_shift-=1
    for i in range(0,len(newSpawn)):
        newSpawn[i][0]+=x_shift
        newSpawn[i][1]+=y_shift
    for i in newSpawn:
        if board[i[0]][i[1]]>7:
            flag=False
            break
    if flag:
        spawn_block=newSpawn
    

def check():
    global board
    global score
    blank_line=[]
    flag=True
    lines_cleared=0
    for i in range(0,20):
        for j in range(0,10):
            if board[i][j]>7:
                flag=False
                break
        if flag:
            blank_line=np.append(blank_line,i)
        flag=True
    for i in range(20):
        if i in blank_line:
            for j in range(i,0,-1):
                board[j]=board[j-1]
            board[0]=np.array([0,0,0,0,0,0,0,0,0,0])

    for i in range(20):
        if np.min(board[i])>7:
            lines_cleared+=1
            board[i]=np.array([0,0,0,0,0,0,0,0,0,0])
    if lines_cleared==4:
        pygame.mixer.Sound.play(tetris_sfx)
        score+=1200
    elif lines_cleared==3:
        pygame.mixer.Sound.play(triple_sfx)
        score+=300
    elif lines_cleared==2:
        pygame.mixer.Sound.play(double_sfx)
        score+=100
    elif lines_cleared==1:
        pygame.mixer.Sound.play(single_sfx)
        score+=30



def restart():
    global board
    restart_text1='G A M E   O V E R'
    text1=font3.render(restart_text1,True,(92,229,193))
    text3=font3.render(restart_text1,True,(230,93,93))
    text1_rect=text1.get_rect()
    text1_rect.center=(350,480)
    restart_text2='PRESS R TO RESTART'
    text2=font4.render(restart_text2,True,(92,229,193))
    text4=font4.render(restart_text2,True,(230,93,93))
    text2_rect=text2.get_rect()
    text2_rect.center=(350,550)
    start_time=pygame.time.get_ticks()
    run=True
    ch=0
    while run:
        for event in pygame.event.get():
            if event.type==QUIT:
                run=False
                ch=1
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                run=False
                ch=1
            if event.type==pygame.KEYDOWN and event.key==pygame.K_r:
                ch=2
                run=False
            if ch==2:
                board=np.array([[0]*10]*20)


        end_time=pygame.time.get_ticks()
        if end_time-start_time<=1000:
            display()
            win.blit(text1,text1_rect)
            win.blit(text2,text2_rect)
        elif end_time-start_time<2000:
            display()
            win.blit(text3,text1_rect)
            win.blit(text4,text2_rect)
        if end_time-start_time>2000:
            start_time=pygame.time.get_ticks()

            
        pygame.time.wait(16)
        pygame.display.update()
    return ch

            



def main():


    win.fill((0,0,0))
    iter_start=pygame.time.get_ticks()
    check_starttime=pygame.time.get_ticks()
    pos_change=0
    rotate_flag=False
    iter_time=250
    run=True
    restart_flag=False
    res=0
    pygame.mixer.music.play(-1)
    spawn()
    while run:
        win.fill((40,40,40))
        for event in pygame.event.get():
            if event.type==QUIT:
                run=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                run=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_RIGHT:
                pos_change=1
            if event.type==pygame.KEYDOWN and event.key==pygame.K_LEFT:
                pos_change=-1
            if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
                rotate_flag=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_DOWN:
                iter_time=100
            if event.type==pygame.KEYUP and event.key==pygame.K_DOWN:
                iter_time=250
        check_endtime=pygame.time.get_ticks()
        

        iter_end=pygame.time.get_ticks()
        if iter_end-iter_start>=iter_time:
            if iteration():
                restart_flag=spawn()
            iter_end=iter_start=pygame.time.get_ticks()
        if check_endtime-check_starttime>=iter_time/8:
            check()
            check_starttime=pygame.time.get_ticks()
        display()

        if restart_flag:
            res=restart()
            iter_time=250
            spawn()
        
        if res==1:
            run=False
        restart_flag=False
        
        if pos_change!=0:
            move(pos_change)
            pos_change=0

        if rotate_flag:
            rotate()
            global r
            r+=1
            rotate_flag=False


        pygame.time.wait(10)
        pygame.display.update()
    pygame.quit()

main()
