import requests
import json

def baralho():
    url = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'
    request = requests.get(url)
    dados = json.loads(request.content)
    print(dados)
    
#baralho()

def tirar_cartas():
    url = f'https://deckofcardsapi.com/api/deck/umbhss77pf1c/draw/?count=2'
    request = requests.get(url)
    dados = json.loads(request.content)
    print(dados) #testem esse print para ver um modo geral.
    cartas = dados["cards"]
    for carta in cartas:
        print(carta['code'])
        
#tirar_cartas() #não esquecam de informar o id

def devolver():
    url = 'http://deckofcardsapi.com/api/deck/79w8khlweeqx/return/'
    request = requests.get(url)
    dados = json.loads(request.content)
    print(dados)
    
#devolver()