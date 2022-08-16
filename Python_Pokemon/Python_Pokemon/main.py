from personagem import *


def criar_jogador():
    nome = input('Qual seu nome? ')
    jogador = Player(nome)
    escolher_pokemon_inicial(jogador)
    jogador.mostrar_pokemons()
    return jogador


def escolher_pokemon_inicial(jogador):
    print(f'Ola {jogador}, voce escolhera agora o Pokemon que ira lhe acompanhar nessa jornada!')

    Pikachu = PokemonEletrico('Pikachu', 1)
    Charmander = PokemonFogo('Charmander', 1)
    Squirtle = PokemonAgua('Squirtle', 1)

    print('Voce possui 3 Pokemon para escolher: ')
    print('1 - ', Pikachu)
    print('2 - ', Charmander)
    print('3 - ', Squirtle)

    while True:
        escolha = input('Escolha o seu! ')
        if escolha == '1':
            jogador.capturar(Pikachu)
            break
        elif escolha == '2':
            jogador.capturar(Charmander)
            break
        elif escolha == '3':
            jogador.capturar(Squirtle)
            break
        else:
            print('Escolha invalida')


player1 = criar_jogador()
player1.mostrar_dinheiro()
inimigo = Inimigo()

player1.batalhar(inimigo)