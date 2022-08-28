import random

import pygame

pygame.init()

RESOLUCAO = (640, 360)

tela = pygame.display.set_mode(RESOLUCAO)


class Fruta:
    cor = (255, 0, 0)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        posicao_x = random.randint(0, 63) * 10
        posicao_y = random.randint(0, 35) * 10
        self.posicao = (posicao_x, posicao_y)

    def desenhar(self, tela_jogo):
        tela_jogo.blit(self.textura, self.posicao)


class Snake:
    cor = (255, 255, 255)
    tamanho = (10, 10)

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        self.corpo = [(100, 100), (90, 100)]

    def desenhar(self, tela_jogo):
        for posicao in self.corpo:
            tela_jogo.blit(self.textura, posicao)

fruta = Fruta()
cobra = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    fruta.desenhar(tela)
    cobra.desenhar(tela)

    pygame.display.update()
