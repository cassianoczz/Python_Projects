import json
import sys

import requests

URL_CONTRIES = 'https://restcountries.com/v2/name'


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print('Erro ao fazer requisicao pais')    
    except Exception as erro:
        print('Erro ao fazer requisicao pais')


def validar_requisicao(resposta_url):
    try:
        if resposta_url:
            return resposta_url
    except:
        print('Erro na validação da requisição')


def parsing(text_resposta_url):
    try:
        return json.loads(text_resposta_url)
    except:
        print('Erro ao fazer parsing da resposta')


def validar_parsing(texto_resposta):
    try:
        if texto_resposta:
            return texto_resposta
    except:
        print('Erro na validação do parsing da resposta')


def mostrar_informacoes(nome_pais, informacao):
    resposta_url = validar_requisicao(requisicao(f'{URL_CONTRIES}/{nome_pais}'))
    resposta_parsing = validar_parsing(parsing(resposta_url))
    for pais_info in resposta_parsing:
        print(f'Pais pesquisado: {pais_info["name"]}, Informação pesquisada: {pais_info[informacao]}')


def menu():
    if len(sys.argv) == 1:
        print('##Bem vindo ao sistema de informações sobre países##')
        print('Uso: python paises.py <nome do pais> <informaçao>')
        print('Informações disponiveis: python paises.py man')

    elif sys.argv[1] == 'man':
        mostrar_manual()

    elif len(sys.argv) == 3:
        pais = sys.argv[1]
        informacao = sys.argv[2]
        mostrar_informacoes(pais, informacao)

    else:
        print('Argumento Invalido')


def mostrar_manual():
    print('Informações disponiveis:')
    print('currencies - Mostra detalhes moedas')
    print('callingCodes - Mostra codigo Area')
    print('capital - Mostra capital')
    print('population - Mostra populacao')
    print('timezones - Mostra fuso horario')


if __name__ == '__main__':
    menu()