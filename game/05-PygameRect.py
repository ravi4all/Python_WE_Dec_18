import pygame
pygame.init()

screen = pygame.display.set_mode((1000,500))
white = 255,255,255
red = 255,0,0

screen.fill(white)

rect = pygame.Rect(0,0,50,50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # screen, color, [x,y,w,h]
    pygame.draw.rect(screen, red, rect)

    pygame.display.update()