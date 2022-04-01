import pygame
pygame.init()

screen = pygame.display.set_mode((800, 700))

x = 75
y = 75
radius = 50
speed = 20

run=True

while run:
    pygame.time.delay(75)

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            run=False

    keys = pygame.key.get_pressed() 

    if keys[pygame.K_LEFT] and x>75:
        x-=speed
    
    if keys[pygame.K_RIGHT] and x<725:
        x+=speed

    if keys[pygame.K_UP] and y>75:
        y-=speed

    if keys[pygame.K_DOWN] and y<625:
        y+=speed

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.update()
pygame.quit()
