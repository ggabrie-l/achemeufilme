import requests
import json

headers = {
    'User-Agent': 'Mozilla/5.0'
}

def localizar():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status()
        endereco_ip = response.json()['ip']

        response = requests.get(f"http://ip-api.com/json/{endereco_ip}")
        response.raise_for_status()
        localizacao = response.json()

        return localizacao
    except Exception as e:
        print(e)

if __name__ == "__main__":
    localizacao_usuario = localizar()

    response = requests.get(f"https://api-content.ingresso.com/v0/theaters?partnership=nome_", headers=headers)
    response2 = response.json()

    city = localizacao_usuario['city']
    regionName = localizacao_usuario['regionName']

    for d in response2:
        if d['state'] == regionName and d['cityName'] == city:
            print(f'Shopping : {d['name']}, em {d['neighborhood']} é o cinema mais perto de você!')
            

        