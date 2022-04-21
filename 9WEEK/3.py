import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 700))
screen.fill((255,255,255))
clock = pygame.time.Clock()
dots = []

done = False
rectangle = False
circle = False
triangle = False
rhombus = False
motion = False

color = (0, 0, 0)
z = 0
x1 = x2 = y1 = y2 = 0
rad = 8
surf = pygame.Surface((1100, 600))

bg = pygame.image.load("design.png")
rect_enable = pygame.image.load("rect_enable.png")
rect_rect = rect_enable.get_rect()
rect_rect.center = (-100, -100)
circle_enable = pygame.image.load("circle_enable.png")
circle_rect = circle_enable.get_rect()
circle_rect.center = (-100, -100)
tri_enable = pygame.image.load("tri_enable.png")
triangle_rect = tri_enable.get_rect()
triangle_rect.center = (-100, -100)
rhombus_enable = pygame.image.load("rhombus_enable.png")
rhombus_rect = rhombus_enable.get_rect()
rhombus_rect.center = (-100, -100)

screen.blit(bg, (0, 0))
surf.fill((255,255,255))
screen.blit(surf, (-1, 100))
pygame.display.update()

def draw_rect():
    if x1 < x2 and y1 < y2:
        pygame.draw.line(screen, color, [x1, y1 - 7], [x1, y2 + 8], 2 * rad)
        pygame.draw.line(screen, color, [x1, y1], [x2 + 8, y1], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2 + 8], [x2, y1], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2], [x1, y2], 2 * rad)
    if x1 > x2 and y1 > y2:
        pygame.draw.line(screen, color, [x1, y1 + 8], [x1, y2 - 7], 2 * rad)
        pygame.draw.line(screen, color, [x1, y1], [x2, y1], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2 - 7], [x2, y1 + 8], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2], [x1, y2], 2 * rad)
    if x1 < x2 and y1 > y2:
        pygame.draw.line(screen, color, [x1, y1 + 8], [x1, y2 - 7], 2 * rad)
        pygame.draw.line(screen, color, [x1, y1], [x2, y1], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2 - 7], [x2, y1 + 8], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2], [x1, y2], 2 * rad)
    if x1 > x2 and y1 < y2:
        pygame.draw.line(screen, color, [x1, y1 - 7], [x1, y2 + 8], 2 * rad)
        pygame.draw.line(screen, color, [x1, y1], [x2, y1], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2 + 8], [x2, y1 - 7], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2], [x1, y2], 2 * rad)
def draw_circle():
    if x1 < x2 and y1 < y2:
        pygame.draw.ellipse(screen, color, (x1, y1, x2 - x1, y2 - y1), 2 * rad)
    if x1 > x2 and y1 < y2:
        pygame.draw.ellipse(screen, color, (x2, y1, x1 - x2, y2 - y1), 2 * rad)
    if x1 < x2 and y1 > y2:
        pygame.draw.ellipse(screen, color, (x1, y2, x2 - x1, y1 - y2), 2 * rad)
    if x1 > x2 and y1 > y2:
        pygame.draw.ellipse(screen, color, (x2, y2, x1 - x2, y1 - y2), 2 * rad)
def draw_triangle():
    if x1 < x2 and y1 < y2:
        pygame.draw.line(screen, color, [x1 - 7, y2 + rad], [x2 + 8, y2 + rad], 2 * rad)
        pygame.draw.line(screen, color, [x1, y2], [(x1 + x2) / 2, y1], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2], [(x1 + x2) / 2, y1], 2 * rad)
    if x1 > x2 and y1 < y2:
        pygame.draw.line(screen, color, [x1 + 8, y2 + rad], [x2 - 7, y2 + rad], 2 * rad)
        pygame.draw.line(screen, color, [x1, y2], [(x1 + x2) / 2, y1], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2], [(x1 + x2) / 2, y1], 2 * rad)
    if x1 < x2 and y1 > y2:
        pygame.draw.line(screen, color, [x1 - 7, y2 - rad], [x2 + 8, y2 - rad], 2 * rad)
        pygame.draw.line(screen, color, [x1, y2], [(x1 + x2) / 2, y1], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2], [(x1 + x2) / 2, y1], 2 * rad)
    if x1 > x2 and y1 > y2:
        pygame.draw.line(screen, color, [x1 + 8, y2 - rad], [x2 - 7, y2 - rad], 2 * rad)
        pygame.draw.line(screen, color, [x1, y2], [(x1 + x2) / 2, y1], 2 * rad)
        pygame.draw.line(screen, color, [x2, y2], [(x1 + x2) / 2, y1], 2 * rad)
def draw_rhombus():
    pygame.draw.line(screen, color, [(x1 + x2) / 2, y1], [x1, (y1 + y2) / 2], 2 * rad)
    pygame.draw.line(screen, color, [(x1 + x2) / 2, y1], [x2, (y1 + y2) / 2], 2 * rad)
    pygame.draw.line(screen, color, [(x1 + x2) / 2, y2], [x1, (y1 + y2) / 2], 2 * rad)
    pygame.draw.line(screen, color, [(x1 + x2) / 2, y2], [x2, (y1 + y2) / 2], 2 * rad)

# main loop
while not done:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            z = 1
        elif event.type == pygame.MOUSEBUTTONUP:
            z = 0
        if event.type == pygame.MOUSEBUTTONDOWN and 25 < y < 75:
            if 25 < x < 75:
                color = (255, 255, 255) # eraser
            elif 100 < x < 150:
                color = (0, 0, 0) # black
            elif 175 < x < 225:
                color = (255, 0, 0) # red
            elif 250 < x < 300:
                color = (0, 0 , 255) # blue
            elif 325 < x < 375:
                color = (0, 255, 0) # green
            elif 400 < x < 450:
                color = (0, 255, 255) # cyan
            elif 475 < x < 525:
                color = (255, 20, 147) # deeppink
            elif 550 < x < 600:
                color = (255, 255, 0) # yellow
            elif 625 < x < 675:
                color = (165, 42, 42) # brown
            elif 700 < x < 750:
                color = (255, 165, 0) # orange
            elif 775 < x < 825:
                color = (128, 0, 128) # purple
            elif 850 < x < 900:
                color = (255, 192, 203) # pink 
            elif 925 < x < 975:
                color = (65, 105, 225) # royalblue
            elif 1000 < x < 1050:
                color = (154, 205, 50) # yellowgreen

        if event.type == pygame.MOUSEBUTTONDOWN and 125 < y < 175 and 1125 < x < 1175:
            rectangle = not rectangle
            circle = False
            triangle = False
            rhombus = False
            if rectangle:
                circle_rect.center = (-100, -100)
                rect_rect.center = (1150, 150)
                triangle_rect.center = (-100, -100)
                rhombus_rect.center = (-100, -100)
                screen.blit(bg, (0, 0))
            else:
                rect_rect.center = (-100, -100)
                screen.blit(bg, (0, 0))
        if rectangle:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = event.pos
                if y1 < 100: 
                    y1 = 106
                if x1 > 1100:
                    x1 = 1091
            if event.type == pygame.MOUSEMOTION and z == 1:
                motion = True
                x2, y2 = event.pos
            if y2 > 100 and x2 < 1100 and z == 0 and motion:
                draw_rect()
                motion = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and 225 < y < 275 and 1125 < x < 1175:
            circle = not circle
            rectangle = False
            triangle = False
            rhombus = False
            if circle:
                rect_rect.center = (-100, -100)
                circle_rect.center = (1150, 250)
                triangle_rect.center = (-100, -100)
                rhombus_rect.center = (-100, -100)
                screen.blit(bg, (0, 0))
            else:
                circle_rect.center = (-100, -100)
                screen.blit(bg, (0, 0))
        if circle:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = event.pos
                if y1 < 100:
                    y1 = 106
                if x1 > 1100:
                    x1 = 1091
            if event.type == pygame.MOUSEMOTION and z == 1:
                motion = True
                x2, y2 = event.pos
            if y2 > 100 and x2 < 1100 and z == 0 and motion:
                draw_circle()
                motion = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and 325 < y < 375 and 1125 < x < 1175:
            triangle = not triangle
            circle = False
            rectangle = False
            rhombus = False
            if triangle:
                triangle_rect.center = (1150, 350)
                circle_rect.center = (-100, -100)
                rect_rect.center = (-100, -100)
                rhombus_rect.center = (-100, -100)
                screen.blit(bg, (0, 0))
            else:
                triangle_rect.center = (-100, -100)
                screen.blit(bg, (0, 0))
        if triangle:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = event.pos
                if y1 < 100: 
                    y1 = 106
                if x1 > 1100:
                    x1 = 1091
            if event.type == pygame.MOUSEMOTION and z == 1:
                motion = True
                x2, y2 = event.pos
            if y2 > 100 and x2 < 1100 and z == 0 and motion:
                draw_triangle()
                motion = False

        if event.type == pygame.MOUSEBUTTONDOWN and 425 < y < 475 and 1125 < x < 1175:
            rhombus = not rhombus
            circle = False
            triangle = False
            rectangle = False
            if rhombus:
                circle_rect.center = (-100, -100)
                rect_rect.center = (-100, -100)
                triangle_rect.center = (-100, -100)
                rhombus_rect.center = (1150, 450)
                screen.blit(bg, (0, 0))
            else:
                rhombus_rect.center = (-100, -100)
                screen.blit(bg, (0, 0))
        if rhombus:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = event.pos
                if y1 < 100: 
                    y1 = 106
                if x1 > 1100:
                    x1 = 1091
            if event.type == pygame.MOUSEMOTION and z == 1:
                motion = True
                x2, y2 = event.pos
            if y2 > 100 and x2 < 1100 and z == 0 and motion:
                draw_rhombus()
                motion = False

        if event.type == pygame.MOUSEBUTTONDOWN and 625 < y < 675 and 1125 < x < 1175:
            surf.fill((255,255,255))
            screen.blit(surf, (-1, 100))
            pygame.display.update()

    if z == 1 and y > 116 and x < 1100:
        if color == (255, 255, 255) and y > 132 and x < 1092:
            rad = 16
        elif not rectangle and not circle and not triangle:
            rad = 8
        if not rectangle and not circle and not triangle and not rhombus:
            dots.append({"color": color, "coords": [x, y]})
    for dot in dots:
        pygame.draw.circle(screen, dot["color"], (dot["coords"][0], dot["coords"][1]), rad)
    for i in range(len(dots) - 1):
        pygame.draw.line(screen, dots[i]["color"], dots[i]["coords"], dots[i + 1]["coords"], 2 * rad)
    if z == 0:
        dots.clear()
    screen.blit(rect_enable, rect_rect)
    screen.blit(circle_enable, circle_rect)
    screen.blit(tri_enable, triangle_rect)
    screen.blit(rhombus_enable, rhombus_rect)
    pygame.display.update()
    clock.tick(240) # FPS