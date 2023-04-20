import pygame as p
import sys
from pygame.locals import *
import time, random
p.init()
WIDTH = 400
HEIGHT = 600
#get color
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = p.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
background = p.image.load("racer/AnimatedStreet.png")
p.display.set_caption("Racer")
font= p.font.SysFont("Verdana", 30)
FPS = 60
clock = p.time.Clock()
SPEED = 10
score = 0
coin = 0
just = 0
#INC_SPEED = p.USEREVENT + 1
#create common template for enemy(opposite car)
class Enemy(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = p.image.load("racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
    def move(self):
        global score
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, WIDTH - 30), 0)
#create our players control of the car
class Player(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = p.image.load("racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = p.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

#create common template of random coins in random coordinate
class Coin(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = p.transform.scale(p.image.load("racer/coin.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, WIDTH - 30), 0)
    def move(self):
        self.rect.move_ip(0, SPEED - 3)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, WIDTH - 30), 0)
#create the same class for bonus coin
class CoinRed(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = p.transform.scale(p.image.load("racer/RedCoin.png"), (45, 45))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(30, WIDTH - 30), 0)
    def move(self):
        self.rect.move_ip(0, SPEED - 3)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, WIDTH - 30), 0)

# give characters to variable
E1 = Enemy()
P1 = Player()
C1 = Coin()
CR1 = CoinRed()
#create some groups
enemies = p.sprite.Group()
enemies.add(E1)
coins = p.sprite.Group()
coins.add(C1)
redcoins = p.sprite.Group()
redcoins.add(CR1) 
all_sprites = p.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)
reserter = 1 # create the variable for counting number, and when number has current value its activate bonus coins.
#put music for relax
p.mixer.music.load('racer/race.mp3')
p.mixer.music.play(-1)
while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
        #if event.type == INC_SPEED:
            #SPEED += 1
    screen.blit(background, (0, 0))# draw background
    COINS = font.render(str(coin), True, BLACK)
    if reserter >= 6:#for increasing speed
        FPS += 10
        reserter = 1
        just += 1
    if just >= 1 :#for appear bonus coin
        screen.blit(CR1.image, CR1.rect)
        CR1.move()
        if reserter % 2 == 0:
            just -= 1
    screen.blit(COINS, (10, 10))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
        if p.sprite.spritecollideany(P1, enemies):
            p.mixer.music.stop()
            p.mixer.Sound('racer/crash.wav').play()
            time.sleep(0.5)
            GameOver = p.transform.scale(p.image.load("racer/gameover.jpg"), (WIDTH, HEIGHT))
            screen.blit(GameOver, (0, 0))
            p.display.update()
            for entity in all_sprites:
                entity.kill()
            time.sleep(2)
            p.quit()
            sys.exit()
        if p.sprite.spritecollideany(P1, coins):
            p.mixer.Sound('racer/coin.mp3').play()
            coin += 1
            reserter += 1
            C1.rect.top = 600
        if p.sprite.spritecollideany(P1,redcoins):#check player's car touch bonus coin 
            p.mixer.Sound('racer/coin.mp3').play()
            coin += 3
            reserter += 1
            CR1.rect.top = 600
    p.display.flip()
    clock.tick(FPS)