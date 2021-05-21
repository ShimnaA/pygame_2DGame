import pygame
pygame.init()

gameSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")

x = 50
y = 50
width = 50
height = 20
velocity = 5

running = True
while running:
    pygame.time.delay(100)  # 100 milli second (0.1second) delay. simpler way to create a clock.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity

    gameSurface.fill((0,0,0))
    pygame.draw.rect(gameSurface, (0,255,0), (x, y, width, height))
    pygame.display.update()

pygame.quit()

