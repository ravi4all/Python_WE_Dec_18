import pygame
pygame.init()

# screen
screen = pygame.display.set_mode((1000,500))
white = 255,255,255
red = 255,0,0

screen.fill(white)

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            # to quit pygame
            pygame.quit()
            # to quit python
            quit()

    pygame.display.update()