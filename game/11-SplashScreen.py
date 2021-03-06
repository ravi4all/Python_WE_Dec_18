import pygame, random
from pygame.locals import *
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))
white = 255,255,255
red = 255,0,0
black = 0,0,0

img = pygame.image.load('frog.png')
bg_music = pygame.mixer.Sound('bg_music.wav')
bg_music.play(-1)

coin_collect = pygame.mixer.Sound('point.wav')

def home():
    font = pygame.font.SysFont(None, 100)
    text = font.render('Welcome to Snake Game',True, black)

    font_1 = pygame.font.SysFont(None, 70)
    text_1 = font_1.render('Press Space to Start', True, black)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.fill(white)
        screen.blit(text, (100,100))
        screen.blit(text_1, (200, 200))
        pygame.display.update()

def gameOver():
    font = pygame.font.SysFont(None, 50)
    text = font.render('Game Over',True, black)

    font_1 = pygame.font.SysFont(None, 40)
    text_1 = font_1.render('Press Space to Start', True, black)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        # screen.fill(white)
        screen.blit(text, (100,100))
        screen.blit(text_1, (200, 200))
        pygame.display.update()

def score(s):
    font = pygame.font.SysFont(None,30)
    text = font.render('Score : {}'.format(s), True, black)
    screen.blit(text, (100,10))

def timer(t):
    font = pygame.font.SysFont(None, 30)
    text = font.render('Timer : {}'.format(t), True, black)
    screen.blit(text, (700, 10))

def snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen, red, [snakeList[i][0],
                         snakeList[i][1], 50, 50])

def game():
    x = 0
    y = 0
    moveX = 0
    moveY = 0
    random_x = random.randint(0, width - 50)
    random_y = random.randint(0, height - 50)
    counter = 0

    snakeList = []
    snakeLength = 1

    FPS = 150
    clock = pygame.time.Clock()
    pygame.time.set_timer(USEREVENT,1000)
    seconds = 30
    while True:
        rect = pygame.Rect(x, y, 50, 50)
        rect_2 = pygame.Rect(random_x, random_y, 50, 50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 3
                    moveY = 0
                elif event.key == pygame.K_LEFT:
                    moveX = -3
                    moveY = 0
                elif event.key == pygame.K_DOWN:
                    moveY = 3
                    moveX = 0
                elif event.key == pygame.K_UP:
                    moveY = -3
                    moveX = 0

        screen.fill(white)
        # pygame.draw.rect(screen, red, rect)
        screen.blit(img, (random_x, random_y))
        x += moveX
        y += moveY

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)

        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        snake(snakeList)

        for each in snakeList[:-1]:
            if each == snakeList[-1]:
                gameOver()

        if rect.colliderect(rect_2):
            random_x = random.randint(0, width - 50)
            random_y = random.randint(0, height - 50)
            coin_collect.play()
            counter += 1
            FPS += 5
            snakeLength += 6

        score(counter)
        timer(seconds)

        if x > width:
            x = -50
        elif x < -50:
            x = width
        elif y > height:
            y = -50
        elif y < -50:
            y = height

        pygame.display.update()
        clock.tick(FPS)

# game()
home()