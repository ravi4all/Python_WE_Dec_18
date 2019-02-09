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

moveX = 1
moveY = 1

while True:
    rect = pygame.Rect(x, y, 50, 50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # screen, color, [x,y,w,h]
    screen.fill(white)
    pygame.draw.rect(screen, red, rect)
    x += moveX
    y += moveY

    if x > width - 50:
        moveX = -1
    elif x < 0:
        moveX = 1
    elif y > height - 50:
        moveY = -1
    elif y < 0:
        moveY = 1

    pygame.display.update()