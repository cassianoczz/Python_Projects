import random

import pygame

pygame.init()

RESOLUCAO = (640, 360)

tela = pygame.display.set_mode(RESOLUCAO)


class Fruta():
    cor = (255, 0, 0)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        posicao_x = random.randint(0, 63) * 10
        posicao_y = random.randint(0, 35) * 10
        self.posicao = (posicao_x, posicao_y)


class Snake():
    cor = (255, 255, 255)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        self.posicao = [(100, 100), (90, 100)]


fruta = Fruta()
cobra = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    tela.blit(fruta.textura, fruta.posicao)

    for posicao in cobra.posicao:
        tela.blit(cobra.textura,posicao)

    pygame.display.update()
