import random

import pygame

pygame.init()

RESOLUCAO = (640,360)

tela = pygame.display.set_mode(RESOLUCAO)

class Frutinha():
    cor = (255,0,0)
    tamanho = (10,10)


    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        posicao_x = random.randint(0, 63) * 10
        posicao_y = random.randint(0, 35) * 10
        self.posicao = (posicao_x, posicao_y)


frutinha = Frutinha()






while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    tela.blit(frutinha.textura, frutinha.posicao)
    pygame.display.update()