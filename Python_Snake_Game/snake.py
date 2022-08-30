import random
import time

import pygame


class Snake:
    cor = (255, 255, 255)
    tamanho = (20, 20)
    velocidade = 20

    def __init__(self):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)
        self.corpo = [(100, 100), (90, 100)]
        self.direcao = 'direita'
        self.pontos = 0

    def desenhar(self, tela_jogo):
        for posicao in self.corpo:
            tela_jogo.blit(self.textura, posicao)

    def andar(self):

        cabeca = self.corpo[0]
        cabeca_x = cabeca[0]
        cabeca_y = cabeca[1]

        if self.direcao == 'direita':
            self.corpo.insert(0, (cabeca_x + self.velocidade, cabeca_y))
        if self.direcao == 'esquerda':
            self.corpo.insert(0, (cabeca_x - self.velocidade, cabeca_y))
        if self.direcao == 'cima':
            self.corpo.insert(0, (cabeca_x, cabeca_y - self.velocidade))
        if self.direcao == 'baixo':
            self.corpo.insert(0, (cabeca_x, cabeca_y + self.velocidade))

        self.corpo.pop(-1)

    def direita(self):
        if self.direcao != 'esquerda':
            self.direcao = 'direita'

    def esquerda(self):
        if self.direcao != 'direita':
            self.direcao = 'esquerda'

    def cima(self):
        if self.direcao != 'baixo':
            self.direcao = 'cima'

    def baixo(self):
        if self.direcao != 'cima':
            self.direcao = 'baixo'

    def colisao_parede_corpo(self):
        cabeca = self.corpo[0]
        cabeca_x = cabeca[0]
        cabeca_y = cabeca[1]

        calda = self.corpo[1:]
        return cabeca_x < 0 or cabeca_y < 0 or cabeca_x > RESOLUCAO[0] or cabeca_y > RESOLUCAO[1] or cabeca in calda

    def colisao_fruta(self, fruta):
        return self.corpo[0] == fruta.posicao

    def comer_fruta(self):
        self.corpo.append((-1, -1))
        self.pontos += 1
        pygame.display.set_caption(f'Snake Game | Pontos: {self.pontos}')


class Fruta:
    cor = (255, 0, 0)
    tamanho = (20, 20)

    def __init__(self, cobra):
        self.textura = pygame.Surface(self.tamanho)
        self.textura.fill(self.cor)

        self.posicao = Fruta.criar_posicao(cobra)

    @staticmethod
    def criar_posicao(cobra):
        posicao_x = random.randint(0, 30) * 20
        posicao_y = random.randint(0, 16) * 20

        if (posicao_x, posicao_y) in cobra.corpo:
            Fruta.criar_posicao(cobra)
        else:
            return posicao_x, posicao_y

    def desenhar(self, tela_jogo):
        tela_jogo.blit(self.textura, self.posicao)


if __name__ == "__main__":
    # Configurações do Jogo
    pygame.init()
    FPS = 10  # CONFIGURAÇÃO QUADROS POR SEGUNDO, TAXA DE ATUALIZAÇÃO DA TELA
    fpsClock = pygame.time.Clock()
    RESOLUCAO = (640, 360)
    TELA = pygame.display.set_mode(RESOLUCAO)
    pygame.display.set_caption('Snake Game')
    PRETO = (0, 0, 0)

    cobra = Snake()
    fruta = Fruta(cobra)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cobra.cima()
                    break
                elif event.key == pygame.K_DOWN:
                    cobra.baixo()
                    break
                elif event.key == pygame.K_LEFT:
                    cobra.esquerda()
                    break
                elif event.key == pygame.K_RIGHT:
                    cobra.direita()
                    break

        if cobra.colisao_fruta(fruta):
            cobra.comer_fruta()
            fruta = Fruta(cobra)

        if cobra.colisao_parede_corpo():
            cobra = Snake()

        cobra.andar()

        TELA.fill(PRETO)
        fruta.desenhar(TELA)
        cobra.desenhar(TELA)

        pygame.display.update()
        fpsClock.tick(FPS)
