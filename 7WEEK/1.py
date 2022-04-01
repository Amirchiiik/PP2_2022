import pygame
from datetime import datetime
current_datetime = datetime.now()
sec = current_datetime.second
min = current_datetime.minute
print(sec)
print(min)


pygame.init()

screen = pygame.display.set_mode((577, 433))
background = pygame.image.load('Mickey.jpeg').convert()
right = pygame.image.load('Right.png').convert()
left = pygame.image.load('Left.png').convert()

surf1 = pygame.Surface((577, 433))
surf1.set_colorkey((0, 0, 0))
surf = pygame.Surface((577, 433))
surf.set_colorkey((0, 0, 0))
pygame.display.flip()
run = True

cnt = sec*6
angle = sec*6*(-1) + 54
angle1 = min*6*(-1) + 306

while run:
    pygame.time.delay(1000)
    angle -= 6
    cnt += 6

    screen.blit(background, (0, 0))
    screen.blit(surf, (0, 0))
    surf.blit(pygame.transform.rotate(right, angle), pygame.transform.rotate(right, angle).get_rect(center=(577/2, 433/2)))
    screen.blit(surf1, (0, 0))
    surf1.blit(pygame.transform.rotate(left, angle1), pygame.transform.rotate(left, angle1).get_rect(center=(577/2, 433/2)))

    if cnt == 360:
        cnt = 0
        angle1 -= 6
    
    pygame.display.flip() 
    
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            run = False

pygame.quit()