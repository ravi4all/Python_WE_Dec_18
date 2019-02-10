import pygame, random
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

x = 0
y = 0
rect = pygame.Rect(x,y,50,50)

moveX = 0
moveY = 0

random_x = random.randint(0,width-50)
random_y = random.randint(0,height-50)

while True:
    rect = pygame.Rect(x, y, 50, 50)
    rect_2 = pygame.Rect(random_x, random_y, 50, 50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0

    # screen, color, [x,y,w,h]
    screen.fill(white)
    pygame.draw.rect(screen, red, rect)
    # pygame.draw.rect(screen, black, rect_2)
    screen.blit(img, (random_x, random_y))
    x += moveX
    y += moveY

    if rect.colliderect(rect_2):
        random_x = random.randint(0, width - 50)
        random_y = random.randint(0, height - 50)
        coin_collect.play()

    if x > width:
        # moveX = -1
        x = -50
    elif x < -50:
        x = width
    elif y > height:
        # moveY = -1
        y = -50
    elif y < -50:
        y = height

    pygame.display.update()