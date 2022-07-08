'''
Este código foi escrito para acessar uma API REST via HTTP POST
'''


import json
import requests

url = "https://d4wezrjrlf.execute-api.us-east-1.amazonaws.com/Versao2"
x = {
  "from": "Eliel - em Python do Notebook da casa do Goya",
  "bid": 310.00
}
data_json = json.dumps(x)
headers = {'Content-type': 'application/json'}
response = requests.post(url, data=data_json, headers=headers)

print(response.text)
