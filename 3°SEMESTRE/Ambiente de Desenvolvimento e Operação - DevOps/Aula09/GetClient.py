'''
Este código foi escrito para acessar uma API REST via HTTP GET
'''


import json
import requests

url = "https://tlqfsgoqta.execute-api.us-east-1.amazonaws.com/Inicial/"
x = {
  "from": "Ana"
}
t = 'from="Ana"'
data_json = json.dumps(x)
headers = {'Content-type': 'application/json'}
response = requests.get(url+t, data=data_json, headers=headers)
