import pygame
pygame.init()

screen = pygame.display.set_mode((1000,500))
white = 255,255,255
red = 255,0,0

screen.fill(white)

img = pygame.Surface((50,50))
img.fill(red)
rect = img.get_rect()
rect.x = 10
rect.y = 10
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # screen, color, [x,y,w,h]
    screen.blit(img, (rect.x, rect.y))

    pygame.display.update()