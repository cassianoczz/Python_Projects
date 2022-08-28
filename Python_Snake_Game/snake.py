import pygame

pygame.init()

RESOLUCAO = (640,360)

tela = pygame.display.set_mode(RESOLUCAO)





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()