from xml.etree.ElementTree import QName
import pygame
import random
import time
pygame.init()
RES = 800
SIZE = 30
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255,215,0)
PINK = (255,192,203)
x, y = random.randrange(SIZE, RES - SIZE, SIZE),random.randrange(SIZE, RES - SIZE, SIZE)
apple = random.randrange(SIZE, RES - SIZE, SIZE),random.randrange(SIZE, RES - SIZE, SIZE)
banana =random.randrange(SIZE, RES - SIZE, SIZE),random.randrange(SIZE, RES - SIZE, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 10
score = 0
lvl = 1
cnt = 0
food_cnt = 0
time_cnt_b = 6
time_cnt_a = 10
time = 5
pygame.time.set_timer(pygame.USEREVENT,1000)
apple_img=pygame.image.load('apple.png')
banana_img =pygame.image.load('banana.png')
pygame.init()
surface = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load('bg.jpg').convert()
while True:
    surface.blit(img, (0, 0))
    # drawing snake, apple
    [pygame.draw.rect(surface, YELLOW, (i, j, SIZE - 1, SIZE - 1)) for i, j in snake]
    # pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))
    surface.blit(apple_img,(apple))
    surface.blit(banana_img,(banana))
    # show score
    render_score = font_score.render(f'SCORE: {score}', 1,ORANGE)
    render_lvl =font_score.render(f'LEVEL :{lvl}',1,BLUE)
    surface.blit(render_score, (5, 5))
    surface.blit(render_lvl, (5,40))
    x+= dx*SIZE
    y+= dy*SIZE
    snake.append((x,y))
    snake = snake[-length:]
    #eating food
    if snake[-1] == apple:
            food_cnt += 1
            length += 1
            score += 1
            cnt +=1
            time_cnt_a =10
            apple = random.randrange(SIZE, RES - SIZE, SIZE),random.randrange(SIZE, RES - SIZE, SIZE)
    if snake[-1] == banana:
            food_cnt += 1
            length += 1
            score += 2
            cnt +=2
            time_cnt_b = 6
            banana =random.randrange(SIZE, RES - SIZE, SIZE),random.randrange(SIZE, RES - SIZE, SIZE)
    #game over
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            font_score=pygame.font.SysFont("Verdana",45,bold =True)
            render_end = font_end.render('GAME OVER', 1,ORANGE)
            end_score =font_score.render(f' Your score is {score}',1,PINK)
            surface.blit(render_end, (RES // 2 - 200, RES // 3))
            surface.blit(end_score, (RES // 2 -200, RES // 2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    exit()
    pygame.display.flip()
    #level
    if cnt>=4:
        lvl+=1
        cnt =0
        fps+=3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type ==pygame.USEREVENT:
            time_cnt_b -=1
            time_cnt_a -=1
    if time_cnt_a ==0:
        apple = random.randrange(SIZE, RES - SIZE, SIZE),random.randrange(SIZE, RES - SIZE, SIZE)
        time_cnt_a =10
    if time_cnt_b ==0:
        banana =random.randrange(SIZE, RES - SIZE, SIZE),random.randrange(SIZE, RES - SIZE, SIZE)
        time_cnt_b = 6
    #control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dy!=1:
        dx, dy = 0, -1
    elif key[pygame.K_s] and dy!=-1:
        dx, dy = 0, 1
    elif key[pygame.K_a] and dx!=1:
        dx, dy = -1, 0
    elif key[pygame.K_d] and dx!=-1:
        dx, dy = 1, 0
    clock.tick(fps)



