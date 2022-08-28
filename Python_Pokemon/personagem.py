from pokemon import *
import random

NOMES = ['Misty', 'Tracey', 'Brock', 'May', 'Max', 'Dawn', 'Iris', 'Cilan', 'Clemont', 'Bonnie', 'Serena', 'Lílian',
         'Vitória', 'Kiawe']

POKEMONS = [
    PokemonFogo('Charmander'),
    PokemonFogo('Charmeleon'),
    PokemonFogo('Charizard'),
    PokemonEletrico('Pichu'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Raichu'),
    PokemonAgua('Squirtle'),
    PokemonAgua('Wartortle'),
    PokemonAgua('Blastoise'),
]


class Personagem:

    # Satoshi é a menor unidade de BTC, é 1 satoshi = 1BTC*10^-8
    def __init__(self, nome=None, pokemons=[], satoshis=10):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons
        self.dinheiro = satoshis

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print(f'Pokemons de {self}')
            for indice, pokemon in enumerate(self.pokemons):
                print(f'{indice} - {pokemon}')
        else:
            print(f'{self} não tem nenhum pokemon')

    def mostrar_dinheiro(self):
        print(f'Seu saldo de Sats é: {self.dinheiro}')

    def ganhar_dinheiro(self, satoshis):
        self.dinheiro += satoshis
        print(f'Voce conquistou {satoshis} Sats')
        self.mostrar_dinheiro()

    def perder_dinheiro(self, satoshis):
        self.dinheiro -= satoshis
        print(f'Voce perdeu {satoshis} Sats')
        self.mostrar_dinheiro()

    def batalhar(self, inimigo):
        print(f'{self} iniciou uma batalha com {inimigo}')

        inimigo.mostrar_pokemons()
        pokemon_inimigo = inimigo.escolher_pokemon()

        pokemon = self.escolher_pokemon()

        while True:
            if pokemon.atacar(pokemon_inimigo):
                print(f'{self} ganhou a batalha')
                self.ganhar_dinheiro(pokemon_inimigo.level * 1.5)
                break
            if pokemon_inimigo.atacar(pokemon):
                print(f'{inimigo} ganhou a batalha')
                self.perder_dinheiro(pokemon_inimigo.level * 0.8)
                break


class Player(Personagem):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f'{self} capturou {pokemon}')

    def explorar(self):
        if random.random() <= 0.2:
            pokemon = random.choice(POKEMONS)
            print(f'Um {pokemon} selvagem apareceu!')

            escolha = input('Deseja capturar (s/n): ')
            if escolha == 's':
                if random.random() > 0.5:
                    self.capturar(pokemon)
            else:
                print('Ok, boa viagem!')

        else:
            print('Voce não encontrou nenhum Pokemon!')

    def escolher_pokemon(self):
        self.mostrar_pokemons()

        while True:
            escolha = input('Escolha algum Pokemon: ')

            try:
                escolha = int(escolha)
                pokemon_escolhido = self.pokemons[escolha]
                print(f'{pokemon_escolhido} eu escolho voce!')
                return pokemon_escolhido
            except:
                print('Escolha invalida')


class Inimigo(Personagem):
    tipo = 'inimigo'

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorio = []
            for numeros in range(random.randint(1, 6)):
                pokemons_aleatorio.append(random.choice(POKEMONS))
            super().__init__(nome, pokemons_aleatorio)
        else:
            super().__init__(nome, pokemons)

    def escolher_pokemon(self):
        pokemon_escolhido = random.choice(self.pokemons)
        print(f'{self} escolheu {pokemon_escolhido}')
        return pokemon_escolhido
