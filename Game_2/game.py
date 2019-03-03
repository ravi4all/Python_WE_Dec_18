import pygame
from pygame.locals import *
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

white = 255,255,255
red = 255,0,0
blue = 0,0,255

backgroundMusic = pygame.mixer.Sound('bg_music.wav')
backgroundMusic.play(-1)

def homeScreen():
    font = pygame.font.SysFont(None, 70)
    text = font.render("Welcome to Arkanoid Game",True, red)
    font_1 = pygame.font.SysFont(None,50)
    text_1 = font_1.render("Press SPACE to start game",True,blue)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        screen.fill(white)
        screen.blit(text, (200,100))
        screen.blit(text_1, (250,200))
        pygame.display.update()

def timer(s):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Time Left : {}".format(s), True, red)
    screen.blit(text, (0,0))

def game():
    brickWidth = 100
    brickHeight = 30
    no_of_col = width // brickWidth
    no_of_row = 4

    bricks = []
    for row in range(1,no_of_row + 1):
        for col in range(no_of_col):
            bricks.append(pygame.Rect((col * 110),
                                      (row * 35),
                                      brickWidth,brickHeight))

    barWidth = 150
    barHeight = 25
    bar_x = (width/2) - barWidth/2
    bar_y = height - 30
    moveBarX = 0

    ballRadius = 10
    ballX = bar_x + (barWidth//2)
    ballY = bar_y - 10
    moveBallX = 0
    moveBallY = 0
    moveBall = False
    ballMoving = False

    seconds = 30
    pygame.time.set_timer(USEREVENT, 1000)

    clock = pygame.time.Clock()
    FPS = 100

    while True:
        if not ballMoving:
            ballX = bar_x + (barWidth // 2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT:
                seconds -= 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moveBarX = 4
                elif event.key == pygame.K_LEFT:
                    moveBarX = -4
                elif event.key == pygame.K_SPACE:
                    moveBall = True
                    ballMoving = True
            elif event.type == pygame.KEYUP:
                moveBarX = 0

        screen.fill(white)

        if moveBall:
            moveBallY = -3
            moveBallX = -3
            moveBall = False

        for i in range(len(bricks)):
            pygame.draw.rect(screen, red, bricks[i])

        bar_rect = pygame.draw.rect(screen, red, [bar_x, bar_y,barWidth,barHeight])
        bar_x += moveBarX
        ballX += moveBallX
        ballY += moveBallY

        ball_rect = pygame.draw.circle(screen, blue, [int(ballX), int(ballY)], ballRadius)

        if bar_x > width - barWidth:
            moveBarX = 0
        elif bar_x < 0:
            moveBarX = 0

        if ballMoving:
            if ball_rect.colliderect(bar_rect):
                moveBallY = -3

        for i in range(len(bricks)):
            if bricks[i].colliderect(ball_rect):
                del bricks[i]
                moveBallY = 3
                FPS += 10
                break

        if ballX > width - ballRadius:
            moveBallX = -3
        elif ballX < ballRadius:
            moveBallX = 3
        # elif ballY > bar_y - ballRadius:
        #     moveBallY = -1
        elif ballY < ballRadius:
            moveBallY = 3

        if ballY > height:
            ballX = bar_x + (barWidth // 2)
            ballY = bar_y - 10
            ballMoving = False
            moveBallY = 0
            moveBallX = 0

        timer(seconds)
        pygame.display.update()
        clock.tick(FPS)

# game()
homeScreen()