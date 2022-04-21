import random

import pygame
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (119,0,255)
def main():
    screen = pygame.display.set_mode((800, 600))
    mode = 'red'
    draw_on = False
    last_pos = (0, 0)
    color = (255, 128, 0)
    radius = 1
    radius_of_circle = 10
    width_of_rect = 20
    height_of_rect = 10
    ok = False
    colors = {
        'red': RED,
        'blue': BLUE,
        'green': GREEN,
        'black':BLACK,
        'white':WHITE,
        'yellow':YELLOW,
        'purple':PURPLE
    }

    done = False
    while not done:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        color = colors[mode]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    pass
                if event.key == pygame.K_F4 and alt_held:
                    pass
                #color mode
                if event.key == pygame.K_1:
                    mode = 'red'
                    if ok:
                        radius -=40
                        ok = False
                if event.key == pygame.K_2:
                    mode = 'blue'
                    if ok:
                        radius -=40
                        ok = False
                if event.key == pygame.K_3:
                    mode = 'green'
                    if ok:
                        radius -=40
                        ok = False
                if event.key == pygame.K_4:
                    mode = 'white'
                    if ok:
                        radius -=40
                        ok = False
                if event.key == pygame.K_5:
                    mode = 'yellow'
                    if ok:
                        radius -=40
                        ok = False
                if event.key == pygame.K_6:
                    mode = 'purple'
                    if ok:
                        radius -=40
                        ok = False
                #changing the radius of pen
                if event.key == pygame.K_DOWN:
                    radius -= 1
                if event.key == pygame.K_UP:
                    radius += 1
                #changing the radius of circle
                if event.key == pygame.K_w:
                    radius_of_circle += 30
                    width_of_rect += 30
                    height_of_rect += 30
                if event.key ==pygame.K_s:
                    radius_of_circle -= 30
                    width_of_rect -= 30
                    height_of_rect -= 30
                #eraser
                if event.key == pygame.K_LSHIFT:
                    ok = True
                    mode ='black'
                    radius +=40
                #cleaning the board
                if event.key ==pygame.K_TAB:
                    screen.fill(BLACK)
                #drawing the circle
                if event.key ==pygame.K_c:
                    pygame.draw.circle(screen,color,(pygame.mouse.get_pos()),radius_of_circle,2)
                #drawing the rectangle
                if event.key== pygame.K_v:
                    mouse = pygame.mouse.get_pos()
                    pygame.draw.rect(screen,color,[mouse[0],mouse[1],width_of_rect,height_of_rect],2)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.circle(screen, color, event.pos, radius)
                draw_on = True
            if event.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if event.type == pygame.MOUSEMOTION:
                if draw_on:
                    pygame.draw.line(screen, color, last_pos, event.pos, radius)
                last_pos = event.pos
        pygame.display.flip()

    pygame.quit()

main()