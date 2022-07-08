'''
Este código foi escrito para acessar uma API REST via HTTP POST
'''


import json
import requests

url = "<<COLOQUE AQUI A URL DO ESTÁGIO DO API GATEWAY>>"
x = {
  "from": "Goya - Client Python",
  "bid": 50.00
}
data_json = json.dumps(x)
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=data_json, headers=headers)
