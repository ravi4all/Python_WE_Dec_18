import pygame
pygame.init()

# screen
screen = pygame.display.set_mode((1000,500))
white = 255,255,255
red = 255,0,0

screen.fill(white)

while True:
    pygame.display.update()