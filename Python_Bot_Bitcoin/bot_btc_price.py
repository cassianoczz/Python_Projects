import ssl
import json

import websocket
import bitstamp.client

import credenciais_exemplo


def cliente():
    return bitstamp.client.Trading(username = credenciais_exemplo.USERNAME, key = credenciais_exemplo.KEY, secret = credenciais_exemplo.SECRET)

def comprar(quantidade):
    trading_cliente = cliente()
    trading_cliente.buy_market_order(quantidade)

def ao_abrir(ws):
    print("Aberta")
    json_subscribe = '''
    {
    "event": "bts:subscribe",
    "data": {
        "channel": "live_trades_btcusd"
        }
    }
    '''
    ws.send(json_subscribe)


def ao_fechar(ws, close_status_code, close_msg):
    print("Fechada")


def ao_receber_msg(ws, mensagem):
    mensagem = json.loads(mensagem)
    preco = mensagem['data']['price']
    print('Preço: ', preco)
    ''' 
    It's a joke, mas é uma realidade, quanto não atingir a hiperbitcoinerização, está barato.
    Apenas para testar a função websocket e a biblioteca que implementa a API    
    '''
    while preco != '100000000':
        comprar(quantidade=0.01)

def erro(ws, error):
    print("Erro: ", error)


if __name__ == '__main__':
    ws = websocket.WebSocketApp("wss://ws.bitstamp.net.",
                                   on_open=ao_abrir,
                                   on_message=ao_receber_msg,
                                   on_error=erro,
                                   on_close=ao_fechar
                                )
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
