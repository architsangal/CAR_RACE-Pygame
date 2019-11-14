import pygame
import random
import math
from pygame import mixer

#initialize the pygame
pygame.init()

#creating a screen
width=800
height=600
screen= pygame.display.set_mode((width,height))#screen is a variable

#Background
background = pygame.image.load("background.png")
background = pygame.transform.scale(background,(width,height))

#(Width,Height)
#Title and Icon
pygame.display.set_caption("Dr. Driver")
icon=pygame.image.load("ufo.png") #downloaded from flaticon.com
pygame.display.set_icon(icon)

# Background Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

#player
playerImg = pygame.image.load("player.png") #giving player an image
playerImg = pygame.transform.scale(playerImg, (50, 65))
x = width/2 - 40 #giving player it's starting coordinated
y = height - 50

#TREES
treeImg = []
tree_x = []
tree_y = []
change_tx = []
change_ty = []
num_of_trees = 6

for i in range(num_of_trees):
    Img = pygame.image.load("tree.png") #giving enemy an image
    treeImg.append(Img)#pygame.transform.scale(Img, (50,65)))
    tree_x.append(random.randint(0,width//3)-100) #giving enemy it's starting coordinated
    tree_y.append(-200)
    change_tx.append(0)
    change_ty.append(0)

change_ty[0]=9

#TREES2
treeImg2 = []
tree_x2 = []
tree_y2 = []
change_tx2 = []
change_ty2 = []
num_of_trees2 = 6

for i in range(num_of_trees2):
    Img = pygame.image.load("tree.png") #giving enemy an image
    treeImg2.append(Img)#pygame.transform.scale(Img, (50,65)))
    tree_x2.append(random.randint((2*width//3)+100,width-100)) #giving enemy it's starting coordinated
    tree_y2.append(-200)
    change_tx2.append(0)
    change_ty2.append(0)

change_ty2[0]=9

#Enemies
enemyImg = []
enemy_x = []
enemy_y = []
change_ex = []
change_ey = []
num_of_enemies = 3

for i in range(num_of_enemies):
    Img = pygame.image.load("enemy.png") #giving enemy an image
    enemyImg.append(pygame.transform.scale(Img, (50,65)))
    enemy_x.append(random.randint(width//3,2*width//3 - 50)) #giving enemy it's starting coordinated
    enemy_y.append(-200)
    change_ex.append(0)
    change_ey.append(0)

change_ey[0]=5

#divider
dividerImg = []
divider_x = []
divider_y = []
change_dx = []
change_dy = []
num_of_dividers = 4

for i in range(num_of_dividers):
    Img = pygame.image.load("divider.png") #giving enemy an image
    dividerImg.append(pygame.transform.scale(Img, (15,65)))
    divider_x.append(width//2 - 15) #giving enemy it's starting coordinated
    divider_y.append(-200)
    change_dx.append(0)
    change_dy.append(0)

change_dy[0]=9

#displaying score
score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
# for other fonts use www.dafont.com download and unzip the file and place it in same directory as the game

over_font = pygame.font.Font('freesansbold.ttf',32)

def show_score():
    score = font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(10,10))

def game_over_text(score_value):
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    final_score = over_font.render("Final Score : "+ str(score_value),True,(255,255,255))
    screen.blit(over_text,(width//2-100,height//2-100))
    screen.blit(final_score,(width//2-115,height//2))    

def player(x,y):
    screen.blit(playerImg,(x,y))#blit means to display

def tree(x,y,i):
    screen.blit(treeImg[i],(x,y))#blit means to display

def tree2(x,y,i):
    screen.blit(treeImg2[i],(x,y))#blit means to display

def divider(x,y,i):
    screen.blit(dividerImg[i],(x,y))#blit means to display

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))#blit means to display

changex=0
changey=0

#collision
def isCollision(enemy_x,enemy_y,x,y):
    distance=math.sqrt( pow(enemy_x-x,2) + pow(enemy_y-y,2) )
    if distance < 30:
        return True
    else:
        return False

#game loop
running=True
c=0
while running:

    # RGB - (0,0,0) is (Red,Green,Blue) for th ecolour of display
    #screen.fill((255,255,255))

    #Background
    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changex -= 6
            if event.key == pygame.K_RIGHT:
                changex += 6
            if event.key == pygame.K_UP:
                changey -= 6
            if event.key == pygame.K_DOWN:
                changey += 6
        if event.type == pygame.KEYUP:
            if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                changex=0
                changey=0

    # Boundries is defined.
    if(x<width/3):
        x=width/3
    elif(x>2*width/3-50):
        x=2*width/3-50
    if(y<0):
        y=0
    elif(y>height-100):
        y=height-100

    #divider
    for i in range(num_of_dividers):
        if(divider_y[i] > height):
            divider_y[i] = -100

        if(divider_y[i] >= (height//num_of_dividers-75)-100):
            if(i<num_of_dividers-1):
                 change_dy[i+1]=9

        divider_y[i] += change_dy[i]
        divider(divider_x[i],divider_y[i],i)
    
    #trees
    for i in range(num_of_trees):
        if(tree_y[i] > height):
            tree_x[i] = random.randint(0,width//3-100) #giving enemy it's starting coordinated
            tree_y[i] = 0

        if(tree_y[i] >= (height//num_of_trees-100)-100):
            if(i<num_of_trees-1):
                 change_ty[i+1]=9

        tree_y[i] += change_ty[i]
        tree(tree_x[i],tree_y[i],i)
    

    #trees2
    for i in range(num_of_trees2):
        if(tree_y2[i] > height):
            tree_x2[i] = random.randint((2*width//3)+100,width-100) #giving enemy it's starting coordinated
            tree_y2[i] = 0

        if(tree_y2[i] >= (height//num_of_trees2-100)-100):
            if(i<num_of_trees2-1):
                 change_ty2[i+1]=9

        tree_y2[i] += change_ty2[i]
        tree2(tree_x2[i],tree_y2[i],i)
    
    #new enemy
    for i in range(num_of_enemies):
        if(enemy_y[i] > height):
            enemy_x[i] = random.randint(width//3+50,2*width//3 - 50) #giving enemy it's starting coordinated
            enemy_y[i] = 0
            score_value += 100

        if(enemy_y[i] >= (height//num_of_enemies-100)-100):
            if(i<num_of_enemies-1):
                 change_ey[i+1]=5

        enemy_y[i] += change_ey[i]
        enemy(enemy_x[i],enemy_y[i],i)
        collision=isCollision(enemy_x[i],enemy_y[i],x,y)
        if collision:
            c=1
            explosion_Sound = mixer.Sound("explosion.wav")
            explosion_Sound.play()
            break
    n=0
    if(c==1):
        screen.blit(background,(0,0))
        while(n<3000):
            game_over_text(score_value)
            pygame.display.update()
            n += 1
        exit()
        
    x += changex
    y += changey
    player(x,y)
    show_score()
    pygame.display.update()#updating the display
