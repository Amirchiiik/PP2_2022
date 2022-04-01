import pygame

pygame.init()

pygame.mixer.music.load('1.mp3')
listofmusic=['1.mp3','2.mp3','3.mp3']
cnt = 0
volume = 1.0
pygame.mixer.music.play(0)
pygame.mixer.music.pause()

screen = pygame.display.set_mode((800, 700))
screen.fill((255, 255, 255))
screen.blit(pygame.image.load('1.png'), pygame.image.load('1.png').get_rect(center=(400, 350)))
pygame.display.update()

x = 75
y = 75
radius = 50
speed = 20
run=True
unpause=False

while run:
    pygame.time.delay(75)

    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            run=False

        if action.type == pygame.MOUSEBUTTONDOWN:
            if action.pos[0]>505 and action.pos[0]<600 and action.pos[1]>310 and action.pos[1]<390 and action.button == 1:
                pygame.mixer.music.stop()
                cnt += 1
                if cnt>2:
                    cnt = 0
                pygame.mixer.music.load(listofmusic[cnt])
                pygame.mixer.music.play(0)

            if action.pos[0]>205 and action.pos[0]<295 and action.pos[1]>310 and action.pos[1]<390 and action.button == 1:
                pygame.mixer.music.stop()
                cnt-=1
                if cnt<0:
                    cnt = 2
                pygame.mixer.music.load(listofmusic[cnt])
                pygame.mixer.music.play(0)

            if action.pos[0]>335 and action.pos[0]<380 and action.pos[1]>310 and action.pos[1]<390 and action.button == 1:
                unpause = not unpause
                if unpause:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            
        if action.type == pygame.KEYDOWN:
            if action.key == pygame.K_SPACE:
                unpause = not unpause
                if unpause:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()

            if action.key == pygame.K_F3:
                volume += 0.1
                pygame.mixer.music.set_volume(volume)
            
            if action.key == pygame.K_F2:
                volume -= 0.1
                pygame.mixer.music.set_volume(volume)

    pygame.display.update()
pygame.quit()
