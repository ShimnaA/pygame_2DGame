import pygame
pygame.init()

screen_width = 800
screen_height = 600
gameSurface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")

x = 50
y = 50
width = 20
height = 20
velocity = 5

isJump = False
jumpCount = 10

running = True
while running:
    pygame.time.delay(10)  # 100 milli second (0.1second) delay. simpler way to create a clock.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (x-velocity)>0:
        x -= velocity
    if keys[pygame.K_RIGHT] and (x+width+velocity) < screen_width:
        x += velocity
    if not isJump:
        if keys[pygame.K_UP] and (y-velocity)>0:
            y -= velocity
        if keys[pygame.K_DOWN] and (y + height + velocity) < screen_height:
            y += velocity
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10

    gameSurface.fill((0,0,0))
    pygame.draw.rect(gameSurface, (0,255,0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

