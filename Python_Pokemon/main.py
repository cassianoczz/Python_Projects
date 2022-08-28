import pickle
from personagem import *


def criar_jogador():
    nome = input('Olá, qual o seu nome? ')
    jogador = Player(nome)
    print(f'{jogador}, esse é um mundo habitado por Pokemons, '
          f'a partir de agora sua missão é se tornar um mestre Pokemon!')
    print('Capture o maximo de Pokemons que conseguir e lute contra os seus inimigos!')
    escolher_pokemon_inicial(jogador)
    jogador.mostrar_pokemons()

    print('Parabens, agora você possui um Pokemon, enfrente Gary, seu Inimigo desde o jardim de infancia!')
    gary = Inimigo('Gary', pokemons=[PokemonAgua('Squirtle', level=1)])
    jogador.batalhar(gary)
    salvar_jogo(jogador)
    return jogador


def escolher_pokemon_inicial(jogador):
    print(f'{jogador}, voce escolhera agora o Pokemon que ira lhe acompanhar nessa jornada!')

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


def salvar_jogo(jogador_salvo):
    try:
        with open('database.db', 'wb') as banco_dados:
            pickle.dump(jogador_salvo, banco_dados)
            print('Jogo salvo com sucesso!')
    except:
        print('Erro ao salvar jogo')


def carregar_jogo():
    try:
        with open('database.db', 'rb') as banco_dados:
            jogador_carregado = pickle.load(banco_dados)
            print('Jogo carregado com sucesso!')
            return jogador_carregado
    except:
        print('Erro ao carregar jogo')


def gameplay():
    print('---------------------------------------')
    print('Bem-vindo ao mundo Pokemon de terminal!')
    print('---------------------------------------')
    jogador = carregar_jogo()
    print('---------------------------------------')

    if jogador:
        print(f'{jogador}, voce já possui alguns Pokemons!')
        jogador.mostrar_pokemons()

    if not jogador:
        jogador = criar_jogador()

    while True:
        print('--------------------------------------------------')
        print('1 - Explorar o mundo Pokemon!')
        print('2 - Enfrentar algum inimigo em uma batalha Pokemon')
        print('3 - Pokedex - Mostra Pokemons que possui')
        print('4 - Mostra quanto Sats possui na sua Wallet')
        print('0 - Sair do jogo')
        escolha = input('Sua escolha: ')
        if escolha == '1':
            jogador.explorar()
            salvar_jogo(jogador)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            jogador.batalhar(inimigo_aleatorio)
            salvar_jogo(jogador)
        elif escolha == '3':
            jogador.mostrar_pokemons()
        elif escolha == '4':
            jogador.mostrar_dinheiro()
        elif escolha == '0':
            print('Fechando jogo ...')
            break
        else:
            print('Escolha invalida')


if __name__ == '__main__':

    gameplay()
