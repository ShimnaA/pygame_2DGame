import pygame

pygame.init()

screen_width = 500
screen_height = 480
gameSurface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

walkLeft = [pygame.image.load('images/L1.png'), pygame.image.load('images/L2.png'), pygame.image.load('images/L3.png'),
            pygame.image.load('images/L4.png'), pygame.image.load('images/L5.png'), pygame.image.load('images/L6.png'),
            pygame.image.load('images/L7.png'), pygame.image.load('images/L8.png'), pygame.image.load('images/L9.png')]
walkRight = [pygame.image.load('images/R1.png'), pygame.image.load('images/R2.png'), pygame.image.load('images/R3.png'),
             pygame.image.load('images/R4.png'), pygame.image.load('images/R5.png'), pygame.image.load('images/R6.png'),
             pygame.image.load('images/R7.png'), pygame.image.load('images/R8.png'), pygame.image.load('images/R9.png')]
bg = pygame.image.load('images/bg.jpg')
char = pygame.image.load('images/standing.png')


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, gamesurface):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            gamesurface.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        elif tity.right:
            gamesurface.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            gamesurface.blit(char, (self.x, self.y))
            self.walkCount = 0

running = True


def redrawGameSurface():
    global walkCount
    gameSurface.blit(bg, (0, 0))
    tity.draw(gameSurface)
    pygame.display.update()

tity = Player(300, 410, 64, 64)
while running:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and (tity.x - tity.velocity) > 0:
        tity.x -= tity.velocity
        tity.left = True
        tity.right = False
    elif keys[pygame.K_RIGHT] and (tity.x + tity.width + tity.velocity) < screen_width:
        tity.x += tity.velocity
        tity.left = False
        tity.right = True
    else:
        tity.left = False
        tity.right = False
        tity.walkCount = 0
    if not tity.isJump:
        if keys[pygame.K_SPACE]:
            tity.isJump = True
            tity.left = False
            tity.right = False
            tity.walkCount = 0
    else:
        if tity.jumpCount >= -10:
            neg = 1
            if tity.jumpCount < 0:
                neg = -1
            tity.y -= (tity.jumpCount ** 2) * 0.5 * neg
            tity.jumpCount -= 1

        else:
            tity.isJump = False
            tity.jumpCount = 10

    redrawGameSurface()

pygame.quit()
