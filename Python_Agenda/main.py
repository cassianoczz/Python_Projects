AGENDA = {}


# AGENDA = {'Guilherme': {
#     'telefone': '99999-0000',
#     'email': 'guilherme@github.com',
#     'endereco': 'rua sem nome',
# }, 'Maria': {
#     'telefone': '99999-0001',
#     'email': 'Maria@github.com',
#     'endereco': 'rua com nome',
# }}


def buscar_contato(contato):
    print('Nome:', contato)
    print('Telefone: ', AGENDA[contato]['telefone'])
    print('Email: ', AGENDA[contato]['email'])
    print('Endereço: ', AGENDA[contato]['endereco'])


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print('_________________')
    else:
        print('Nao existem contatos na agenda.')


def incluir_editar_contato(nome, telefone, email, endereco):
    AGENDA[nome] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print(f'Contato {nome} adicionado com sucesso.')


def ler_detalhes_contatos():
    telefone = input('Qual o telefone: ')
    email = input('Qual o email: ')
    endereco = input('Qual o endereco: ')
    return telefone, email, endereco


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print(f'{contato} foi excluido com sucesso')
    except KeyError:
        print('Contato inexistente')
    except:
        print('ocorreu erro inesperado excluir contato')


def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato},{telefone},{email},{endereco}\n')
    except FileNotFoundError:
        print('Arquivo não encontrado')
    except:
        print('ocorreu erro inesperado exportar contatos')


def importar_contatos(arquivo_contatos):
    try:
        with open(arquivo_contatos) as arquivo:
            linhas_arquivo = arquivo.readlines()
            for linha in linhas_arquivo:
                dados = linha.strip().split(',')
                nome = dados[0]
                telefone = dados[1]
                email = dados[2]
                endereco = dados[3]
                incluir_editar_contato(nome, telefone, email, endereco)

    except FileNotFoundError:
        print('Arquivo nao encontrado')
    except:
        print('ocorreu erro inesperado importar contatos')


def salvar():
    exportar_contatos('banco_dados.csv')


def carregar():
    try:
        with open('banco_dados.csv') as arquivo:
            linhas_arquivo = arquivo.readlines()
            for linha in linhas_arquivo:
                dados = linha.strip().split(',')
                AGENDA[dados[0]] = {
                    'telefone': dados[1],
                    'email': dados[2],
                    'endereco': dados[3],
                }
    except FileNotFoundError:
        print('Arquivo nao encontrado')
    except:
        print('ocorreu erro inesperado carregar contatos')


def imprime_menu():
    print('1 - Mostra todos os contatos')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Exluir contato')
    print('6 - Exportar Agenda')
    print('7 - Importar contatos CSV')
    print('0 - Fechar Agenda')


def opcao_menu(opcao):
    if opcao is None:
        imprime_menu()
    elif opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        nome = input('Qual o nome: ')
        buscar_contato(nome)
    elif opcao == '3':
        nome = input('Qual o nome: ')
        try:
            AGENDA[nome]
            print('Contato já existem')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(nome, telefone, email, endereco)
    elif opcao == '4':
        nome = input('Qual o nome: ')
        try:
            AGENDA[nome]
            print('Editando contato: ', nome)
            telefone, email, endereco = ler_detalhes_contatos()
            incluir_editar_contato(nome, telefone, email, endereco)
        except KeyError:
            print('Contato inexistente')
    elif opcao == '5':
        nome = input('Qual o nome: ')
        excluir_contato(nome)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo: ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo: ')
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        salvar()
        print("Agenda Fechada")
    else:
        print('Opção invalida')


carregar()
while True:
    opcao_menu(None)
    opcao_menu(input('Escolha uma opção: '))
