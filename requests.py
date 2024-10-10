import requests
from bs4 import BeautifulSoup

def main():
    MLB_produto = 'MLB2223878983'
    URL = ('https://api.mercadolibre.com/items/' + MLB_produto)
    html = 'https://produto.mercadolivre.com.br/MLB-2223878983-conversores-midia-gigabit-1000-mb-par-a-b-fibra-optica-_JM'

    res = requests.get(html)

    res = requests.get(html)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')

        titulo = soup.find('h1', class_='ui-pdp-title').text
        print('Titulo: ', titulo)

        preco = soup.find('span', class_='andes-money-amount ui-pdp-price__part andes-money-amount--cents-superscript andes-money-amount--compact').text
        print('Preço: ', preco)

        descricao = soup.find('div', class_='ui-pdp-description').text.strip()
        print('Descrição: ', descricao)
    else:
        print('Erro')