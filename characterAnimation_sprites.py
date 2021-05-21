import pygame
pygame.init()

screen_width = 500
screen_height = 480
gameSurface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'), pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'), pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'), pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'), pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')

x = 50
y = 400
width = 64
height = 64
velocity = 5

isJump = False
jumpCount = 10

running = True
left = False
right = False
walkCount = 0

def redrawGameSurface():
    global walkCount
    gameSurface.blit(bg, (0,0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        gameSurface.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        gameSurface.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        gameSurface.blit(char, (x,y))
        walkCount = 0
    pygame.display.update()

while running:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (x-velocity)>0:
        x -= velocity
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and (x+width+velocity) < screen_width:
        x += velocity
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
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

    redrawGameSurface()

pygame.quit()

