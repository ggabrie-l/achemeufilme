import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def localizar():
    try:
        resposta = requests.get("https://api.ipify.org?format=json")
        resposta.raise_for_status()
        endereco_ip = resposta.json()['ip']

        resposta = requests.get(f"http://ip-api.com/json/{endereco_ip}")
        resposta.raise_for_status()
        localizacao = resposta.json()

        return localizacao
    except Exception as e:
        print(e)

def filmes(ids: list):
    shopping_id = ids[0]
    city_id = ids[1]

    resposta = requests.get(f"https://api-content.ingresso.com/v0/sessions/city/{city_id}/theater/{shopping_id}/partnership/null?date=2025-08-25", headers=headers)
    resposta_json = resposta.json()

    filmes_lista = resposta_json[0]['movies']

    print(f"\t** Filmes para hoje  ( {resposta_json[0]['dayOfWeek']} ) ** \n")
    for filme in range(len(filmes_lista)):
        print(f"\t ~ {filmes_lista[filme]['title']}")

if __name__ == "__main__":
    localizacao_usuario = localizar()

    resposta = requests.get(f"https://api-content.ingresso.com/v0/theaters?partnership=nome_", headers=headers)
    resposta_json = resposta.json()

    city = localizacao_usuario['city']
    regionName = localizacao_usuario['regionName']

    for cinema in resposta_json:
        if cinema['state'] == regionName and cinema['cityName'] == city:
            print(f' *** Shopping : {cinema['name']}, em {cinema['neighborhood']} é o cinema mais perto de você! *** \n')

            ids = [cinema['id'], cinema['cityId']]

            filmes(ids)
         
