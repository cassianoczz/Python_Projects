# Crawler Multi Thread

Projeto Crawler realiza a busca o telefone em anuncios de carros do site https://django-anuncios.solyd.com.br/ foi desenvolvido para esse fim.
O Crawler instancia diversas Threads para realizar a operação de forma mais rapida e usa Expressão regular para encontrar os numeros na pagina web, os numeros encotrados são salvos no arquivo telefones.csv.


# Instalação

Instale o pipenv:

```
pip install pipenv
```

Faça o fork ou clone o projeto:
```
git clone git@github.com:<seu_usuario>/Python_Projects.git
```

Navegue até a pasta do projeto:
```
cd ../Python_Projects/Python_Crawler_Multi_Thread
```

Para instalar dependencias com pipenv:
```
pipenv install
```

Executar terminal e siga as instruções:
'''
pipenv run python crawler.py 
'''