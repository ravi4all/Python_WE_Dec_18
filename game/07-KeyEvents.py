import pygame
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))
white = 255,255,255
red = 255,0,0

x = 0
y = 0
rect = pygame.Rect(x,y,50,50)

moveX = 0
moveY = 0

while True:
    rect = pygame.Rect(x, y, 50, 50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
            elif event.key == pygame.K_LEFT:
                moveX = -1
        elif event.type == pygame.KEYUP:
            moveX = 0

    # screen, color, [x,y,w,h]
    screen.fill(white)
    pygame.draw.rect(screen, red, rect)
    x += moveX
    y += moveY

    if x > width - 50:
        moveX = 0
    elif x < 0:
        moveX = 0
    elif y > height - 50:
        moveY = 0
    elif y < 0:
        moveY = 0

    pygame.display.update()