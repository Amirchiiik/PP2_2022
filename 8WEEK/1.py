import pygame
from pygame.locals import *
import random, time

pygame.init()

w, h = 800, 700

color1 = pygame.Color(0, 0, 0)         
color2 = pygame.Color(255, 255, 255)   
color3 = pygame.Color(128, 128, 128)   
color4 = pygame.Color(255, 0, 0)      

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, color1)
your = font.render("Your score is: ", True, color1)
place = your.get_rect(center = (400, 350))
DISPLAYSURF = pygame.display.set_mode((w,h))
background = pygame.image.load("background.png").convert()
background = pygame.transform.scale(background, (w, h))
DISPLAYSURF.blit(background, (0,0)) 
pygame.display.set_caption("Game")
scores = 0
COIN_SPEED = 3.5
COINS = 0 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("car.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 120))
        # self.image.set_colorkey(color1)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 800:       
            if keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)   

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('car_bandit.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 120))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,800-40), 0)

    def move(self):
        global scores
        self.rect.move_ip(0, speed)
        if self.rect.top > 700:
            scores += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 700), 0)

class SmallCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin1.png")
        self.rect  =self.image.get_rect()
        self.rect.center =(random.randint(50, w-50),random.randint(100, h-100))
    def move(self):
        global COINS
        self.rect.move_ip(0,COIN_SPEED)
        if(self.rect.top>600):
            self.rect.top = 0
            self.rect.center = (random.randint(30,w-30),0)

x, y = 350, 600

speed = 5

run = True
P1 = Player()
E1 = Enemy()
C1 = SmallCoin()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

INC_SPEED = pygame.USEREVENT + 1

pygame.time.set_timer(INC_SPEED, 1000)
 
while run:     
    score = font_small.render(str(scores), True, color1)
    scor = font.render(str(scores), True, color1)
    DISPLAYSURF.blit(background, (0,0)) 
    DISPLAYSURF.blit(score, (10,10))

    pygame.time.delay(15)
    
    for event in pygame.event.get():                  
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == INC_SPEED:
            speed += 2
    
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('1.mp3').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(color4)                    
        DISPLAYSURF.blit(game_over, (30, 250))
        DISPLAYSURF.blit(your, place)
        DISPLAYSURF.blit(scor, scor.get_rect(center = (620, 350)))

        pygame.display.update()
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
    if P1.rect.colliderect(C1.rect):
        pygame.mixer.Sound("coin.wav").play()
        COINS += 1
        C1.rect.center =(random.randint(30,w-30),0)
    DISPLAYSURF.blit(C1.image,(364,10))
    img_coin = font_small.render(str(COINS),True,(255, 255, 0))
    DISPLAYSURF.blit(img_coin,(370,45))
    pygame.display.update()
pygame.quit()
