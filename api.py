import requests

from money.model.dollar import Dollar


def api_dollar():
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = requisicao.json()
    return Dollar(
        cotacao['USD']['bid'],
        cotacao['USD']['high'],
        cotacao['USD']['low'],
        cotacao['USD']['create_date']
    )
