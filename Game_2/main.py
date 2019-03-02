import pygame, random
from pygame.locals import *
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))
white = 255,255,255
red = 255,0,0
black = 0,0,0

# bg_music = pygame.mixer.Sound('bg_music.wav')
# bg_music.play(-1)

# coin_collect = pygame.mixer.Sound('point.wav')

def home():
    font = pygame.font.SysFont(None, 100)
    text = font.render('Welcome to Bricks Game',True, black)

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

def game():
    bar = 150
    x = (width / 2) - bar/2
    y = height - 30
    moveX = 0
    counter = 0

    ballX = int(width/2)
    ballY = int(height - 30 - 10)
    
    FPS = 150
    clock = pygame.time.Clock()
    pygame.time.set_timer(USEREVENT,1000)
    seconds = 30
    while True:
        # rect = pygame.Rect(x, y, bar, 30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveX = 5
                elif event.key == pygame.K_LEFT:
                    moveX = -5
            elif event.type == pygame.KEYUP:
                moveX = 0

        screen.fill(white)
        
        pygame.draw.rect(screen, red, [x,y,bar,30])
        pygame.draw.circle(screen, black, [ballX,ballY],10)
        x += moveX
        ballX += moveX

        # score(counter)
        # timer(seconds)

        if x > width - bar or x < 0:
            moveX = 0

        for i in range(0,width - 80, 80):
            for j in range(0,120, 30):
                pygame.draw.rect(screen, red, [i,j,75,25])
            #     j += 30
            # i += 80

        # for row in range(5):
        #     for col in range(15):
        #         pygame.draw.rect(screen, red, [col * 80, row * 40, 70, 35])

        # pygame.draw.rect(screen, red, [0, 0, 80, 30])
        # pygame.draw.rect(screen, red, [81, 0, 80, 30])
        # pygame.draw.rect(screen, red, [162, 0, 80, 30])
        #
        # pygame.draw.rect(screen, red, [0, 31, 80, 30])
        # pygame.draw.rect(screen, red, [0, 62, 80, 30])
        # pygame.draw.rect(screen, red, [0, 93, 80, 30])

        pygame.display.update()
        clock.tick(FPS)

game()
# home()
