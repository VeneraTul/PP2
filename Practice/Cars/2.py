import pygame
import sys
import random, time


pygame.init()


FPS = 60
FramePerSec = pygame.time.Clock()


BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


WIDTH = 400
HEIGHT = 600
SPEED = 5
COINSPEED = 5
SCORE = 0
COINS = 0
LEVEL = 1


font = pygame.font.SysFont("Times New Roman", 60)
font_small = pygame.font.SysFont("Times New Roman", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("Images/AnimatedStreet.png")

 
screen = pygame.display.set_mode((400,600))
screen.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600): 
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.randomCoin = random.randint(1, 3)
        self.image = pygame.image.load("Images/coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,WIDTH-40), 0)
        


    def move(self):
        global COINS
        self.rect.move_ip(0,COINSPEED)
        if (self.rect.bottom > 600): 
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)


        
P1 = Player()
E1 = Enemy()
COIN = Coin()
coin_dup = 0

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(COIN)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(COIN)



def levelAdder():
    global LEVEL
    global SPEED
    if COINS // 4 > LEVEL:
        LEVEL += 1
        SPEED += 3
        print(SPEED)

while True:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    screen.blit(scores, (10,10))
    collected = font_small.render(str(COINS), True, BLACK)
    screen.blit(collected, (400 - 30,10))
    levels = font_small.render(str(LEVEL), True, BLACK)
    screen.blit(levels, (400 - 30, 400 - 30))
    

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
        

    if pygame.sprite.spritecollideany(P1, enemies):
 
                   
          screen.fill(RED)
          screen.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        


    if pygame.sprite.spritecollideany(P1, coins):
            for coin in coins:
                coin.kill()

            randomCoin = random.randint(1, 3)
            if COIN.randomCoin == 1:
                COINS += 1
            if COIN.randomCoin == 2:
                COINS += 2
            if COIN.randomCoin == 3:
                COINS += 3
            pygame.display.update() 
    if(len(coins) == 0): 
        COIN = Coin()
        coins.add(COIN)
        all_sprites.add(COIN)

    levelAdder()

    pygame.display.update()
    FramePerSec.tick(FPS)