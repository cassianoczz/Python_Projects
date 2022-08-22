import re
import threading

import requests
from bs4 import BeautifulSoup

DOMINIO = 'https://django-anuncios.solyd.com.br'
URL_AUTOMOVEIS = 'https://django-anuncios.solyd.com.br/automoveis/'
LINKS_ANUNCIOS_AUTO = []


def buscar(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print('Erro ao acessar URL')
    except Exception as error:
        print('Erro ao acessar URL')
        print(error)


def parsing(resposta_url):
    try:
        if resposta_url:
            soup = BeautifulSoup(resposta_url, 'html.parser')
            return soup
        else:
            print('Erro ao retornar Parsing resposta ')
    except Exception as error:
        print('Erro ao processar a resposta')
        print(error)


def encontrar_links(soup):
    try:
        if soup:
            card_anuncio = soup.find_all('a', class_="card")
            links = []
            for card in card_anuncio:
                link = card['href']
                links.append(link)
            return links
    except:
        print("Erro encontrar links na pagina")


def encontrar_telefones(soup):

    try:
        if soup:
            descricao_anuncio = soup.find_all('div', class_="sixteen wide column")[2].p.get_text().strip()
    except:
        print("Erro encontrar telefones na pagina")
        return None

    regex = re.findall(r'\(?0?([1-9]{2})[ \-\.\)]{0,2}(9[ \-\.]?\d{4})[ \-\.]?(\d{4})', descricao_anuncio)
    if regex:
        return regex


def listar_telefones():
    link_anuncios_auto = LINKS_ANUNCIOS_AUTO.pop(0)
    soup_automoveis = parsing(buscar(DOMINIO+link_anuncios_auto))
    telefones = encontrar_telefones(soup_automoveis)
    if telefones:
        for telefone in telefones:
            print('Telefone Encontrado: ', telefone)
            salvar_telefone(telefone)


def salvar_telefone(telefone):
    string_telefone = f'{telefone[0]}{telefone[1]}{telefone[2]}\n'
    try:
        with open('telefones.csv', 'a') as arquivo:
            arquivo.write(string_telefone)
    except:
        print('Erro ao salvar o arquivo')


if __name__ == '__main__':
    soup_automoveis = parsing(buscar(URL_AUTOMOVEIS))
    LINKS_ANUNCIOS_AUTO = encontrar_links(soup_automoveis)

    THREADS = []
    for indice in range(10):
        thread = threading.Thread(target=listar_telefones)
        THREADS.append(thread)

    for thread_start in THREADS:
        thread_start.start()

    for thread_join in THREADS:
        thread_join.join()




