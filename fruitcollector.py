import pygame
import random
import math
#from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((600, 600))
Background = pygame.image.load('backgrnd.jpg')
icon = pygame.image.load('diet.png')
pygame.display.set_icon(icon)
#mixer.music.load('back_sound.mp3')
#mixer.music.play(-1)
level_game = 1
pygame.display.set_caption('Fruit Collector')
start = 'not started'

# basket
Basket = pygame.image.load('basket.png')
basketX = 260
basketY = 500
basketX_change = 0
basketY_change = 0
state = 'ready'
score = 0
over_font = pygame.font.Font('BENGUIAB.ttf', 55)
font = pygame.font.Font('BENGUIAB.ttf', 24)
g_over = 'not over'
level_font = pygame.font.Font('BENGUIAB.ttf', 24)
pygame.display.set_caption('Fruit ')
# mango
mango_image = []
mangoY = []
# mango_image = pygame.image.load('d:/games/fruit_collector/mango.png')
mangoX = 260
mangoX_change = []
mangoY_change = 0.4
s1 = 0

# pineapple
pineapple_image = []
pineappleY = []
# pineapple_image = pygame.image.load('d:/games/fruit_collector/pineapple.png')
pineappleX = 150
pineappleX_change = []
pineappleY_change = 0.4
s3 = 0

# apple
apple_image = []
appleY = []
# apple_image = pygame.image.load('d:/games/fruit_collector/apple.png')
appleX = 400
appleX_change = []
appleY_change = 0.4
s2 = 0

# banana
banana_image = []
bananaY = []
# banana_image = pygame.image.load('d:/games/fruit_collector/banana.png')
bananaX = 300
bananaX_change = []
bananaY_change = 0.4
s4 = 0

# fruits list
fruits = ['mangoX', 'appleX', 'pineappleX', 'bananaX']
list1 = []
fruitsY = ['mangoY', 'appleY', 'pineappleY', 'bananaY']
speed = 0


def basket(x1, y):
    screen.blit(Basket, (x1, y))


def mango(x2, y, k):
    global state, mango_image
    screen.blit(mango_image[k], (x2, y))
    state = 'ready'


def banana(x3, y, k):
    global state, banana_image
    screen.blit(banana_image[k], (x3, y))
    state = 'ready'


def pineapple(x4, y, k):
    global state, pineapple_image
    screen.blit(pineapple_image[k], (x4, y))
    state = 'ready'


def apple(x5, y, k):
    global state, apple_image
    screen.blit(apple_image[k], (x5, y))
    state = 'ready'


def show_score(x6, y):
    global score
    score_value = font.render('SCORE : ' + str(score), True, (0, 0, 0))
    screen.blit(score_value, (x6, y))


def game_over(x7, y):
    global g_over
    over = over_font.render('GAME OVER', True, (0, 0, 0))
    screen.blit(over, (x7, y))
    g_over = 'over'


def level():
    global level_game
    gamelevel = level_font.render('LEVEL : ' + str(level_game), True, (0, 0, 0))
    screen.blit(gamelevel, (450, 10))


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(Background, (0, 0))
    speed += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                basketX_change = -2

            elif event.key == pygame.K_RIGHT:
                basketX_change = 2

            elif event.key == pygame.K_F1:
                state = 'generate'
                start = 'start'

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                basketX_change = 0

            if event.key == pygame.K_F1:
                state = 'ready'

    # basket controls
    basketX += basketX_change
    if basketX <= 0:
        basketX = 0
    elif basketX >= 535:
        basketX = 535

    # generating fruit

    if state == 'generate':
        x = random.randint(0, 3)
        list1.append(x)
        changeX = random.randint(10, 535)

        if x == 0:
            mango_image.append(pygame.image.load('mango.png'))
            mangoY.append(80)
            mangoX_change.append(changeX)
        if x == 1:
            apple_image.append(pygame.image.load('apple.png'))
            appleY.append(80)
            appleX_change.append(changeX)
        if x == 2:
            pineapple_image.append(pygame.image.load('pineapple.png'))
            pineappleY.append(80)
            pineappleX_change.append(changeX)
        if x == 3:
            banana_image.append(pygame.image.load('banana.png'))
            bananaY.append(80)
            bananaX_change.append(changeX)

    # speed of fruits

    if speed >= 5000 and start == 'start':
        mangoY_change, appleY_change, pineappleY_change, bananaY_change = 6, 6, 6, 6
        state = 'generate'
        level_game = 3
    elif speed >= 3000 and start == 'start':
        mangoY_change, appleY_change, pineappleY_change, bananaY_change = 5, 5, 5, 5
        state = 'generate'
        level_game = 2

    # fruits movement
    s1, s2, s3, s4 = 0, 0, 0, 0
    for i in range(len(list1)):
        if list1[i] == 0:
            if mangoY[s1] <= 600:
                mangoY[s1] += mangoY_change
                mango(mangoX_change[s1], mangoY[s1], s1)
                collide = math.sqrt((math.pow(basketX - mangoX_change[s1], 2)) + (math.pow(basketY - mangoY[s1], 2)))
                if mangoY[s1] == 290:
                    state = 'generate'
                if collide <= 50:
                    score += 1
                    mangoY[s1] = 700
                    mango(mangoX_change[s1], mangoY[s1], s1)
                if mangoY[s1] == 590:
                    game_over(150, 270)
            else:
                pass
            s1 += 1
        elif list1[i] == 1:
            if appleY[s2] <= 600:
                appleY[s2] += appleY_change
                apple(appleX_change[s2], appleY[s2], s2)
                collide = math.sqrt((math.pow(basketX - appleX_change[s2], 2)) + (math.pow(basketY - appleY[s2], 2)))
                if appleY[s2] == 290:
                    state = 'generate'
                if collide <= 50:
                    score += 1
                    appleY[s2] = 700
                    apple(appleX_change[s2], appleY[s2], s2)
                if appleY[s2] == 590:
                    game_over(150, 270)
            else:
                pass
            s2 += 1
        elif list1[i] == 2:
            if pineappleY[s3] <= 600:
                pineappleY[s3] += pineappleY_change
                pineapple(pineappleX_change[s3], pineappleY[s3], s3)
                collide = math.sqrt(
                    (math.pow(basketX - pineappleX_change[s3], 2)) + (math.pow(basketY - pineappleY[s3], 2)))
                if pineappleY[s3] == 290:
                    state = 'generate'
                if collide <= 50:
                    score += 1
                    pineappleY[s3] = 700
                    pineapple(pineappleX_change[s3], pineappleY[s3], s3)
                if pineappleY[s3] == 590:
                    game_over(150, 270)
            else:
                pass
            s3 += 1
        elif list1[i] == 3:
            if bananaY[s4] <= 600:
                bananaY[s4] += bananaY_change
                banana(bananaX_change[s4], bananaY[s4], s4)
                collide = math.sqrt((math.pow(basketX - bananaX_change[s4], 2)) + (math.pow(basketY - bananaY[s4], 2)))
                if bananaY[s4] == 290:
                    state = 'generate'
                if collide <= 50:
                    score += 1
                    bananaY[s4] = 700
                    banana(bananaX_change[s4], bananaY[s4], s4)
                if bananaY[s4] == 590:
                    game_over(150, 270)
            else:
                pass
            s4 += 1

    if g_over == 'over':
       # game_over(150, 270)
        basketX = 700
        basketY = 630
        basket(basketX, basketY)
        running = False
        #print(score)
        #print(level_game)

    show_score(10, 10)
    basket(basketX, basketY)
    level()
    pygame.display.update()

