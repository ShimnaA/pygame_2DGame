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
        self.standing = True
        self.hitbox = (self.x + 17, self.y +11, 29, 52)

    def draw(self, gamesurface):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                gamesurface.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                gamesurface.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                gamesurface.blit(walkLeft[0], (self.x, self.y))
            else:
                gamesurface.blit(walkRight[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 27, 52)
        pygame.draw.rect(gamesurface, (255,0,0), self.hitbox, 2)

class Projectile():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velocity = 8 * facing
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

class Enemy():
    walkLeft =  [pygame.image.load('images/L1E.png'), pygame.image.load('images/L2E.png'),
                 pygame.image.load('images/L3E.png'), pygame.image.load('images/L4E.png'),
                 pygame.image.load('images/L5E.png'), pygame.image.load('images/L6E.png'),
                 pygame.image.load('images/L7E.png'), pygame.image.load('images/L8E.png'),
                 pygame.image.load('images/L9E.png'), pygame.image.load('images/L10E.png'),
                 pygame.image.load('images/L11E.png')]
    walkRight = [pygame.image.load('images/R1E.png'), pygame.image.load('images/R2E.png'),
                 pygame.image.load('images/R3E.png'), pygame.image.load('images/R4E.png'),
                 pygame.image.load('images/R5E.png'), pygame.image.load('images/R6E.png'),
                 pygame.image.load('images/R7E.png'), pygame.image.load('images/R8E.png'),
                 pygame.image.load('images/R9E.png'), pygame.image.load('images/R10E.png'),
                 pygame.image.load('images/R11E.png')]
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.walkCount = 0
        self.velocity =3
        self.path = [self.x, self.end]
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        if self.velocity > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)


    def move(self):
        if self.velocity > 0:
            if self.x + self.velocity < self.path[1]:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.x = self.x + self.velocity
                self.walkCount = 0
        else:
            if self.x + self.velocity > self.path[0]:
                self.x += self.velocity
            else:
                self.velocity *= -1
                self.x = self.x + self.velocity
                self.walkCount = 0

    def hit(self):
        print("enemy hit")


running = True


def redrawGameSurface():
    global walkCount
    gameSurface.blit(bg, (0, 0))
    tity.draw(gameSurface)
    enemy.draw(gameSurface)
    for bullet in bullets:
        bullet.draw(gameSurface)
    pygame.display.update()

tity = Player(300, 410, 64, 64)
bullets = []
enemy = Enemy(100, 410, 64, 64, 450)
shootdelay = 0
while running:
    clock.tick(27)
    if shootdelay > 0:
        shootdelay += 1
    if shootdelay >3:
        shootdelay = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for bullet in bullets:
        if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and \
            bullet.y + bullet.radius > enemy.hitbox[1]:
            if bullet.x + bullet.radius > enemy.hitbox[0] and \
                bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                    enemy.hit()
                    bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.velocity
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootdelay == 0:
        if tity.left:
            facing = -1
        else:
            facing = 1
        if len(bullets)<5:
            bullets.append(Projectile(round(tity.x + tity.width//2), round(tity.y + tity.height//2),
                                      6, (0,0,0), facing))
        shootdelay = 1

    if keys[pygame.K_LEFT] and (tity.x - tity.velocity) > 0:
        tity.x -= tity.velocity
        tity.left = True
        tity.right = False
        tity.standing = False
    elif keys[pygame.K_RIGHT] and (tity.x + tity.width + tity.velocity) < screen_width:
        tity.x += tity.velocity
        tity.left = False
        tity.right = True
        tity.standing = False
    else:
        tity.standing = True
        tity.walkCount = 0

    if not tity.isJump:
        if keys[pygame.K_UP]:
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
