import json
from datetime import datetime

def lambda_handler(event, context):
    # Data e hora para registrar na mensagem
    data_hora = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    # Dados da mensagem vindos via HTTP POST
    # Deve haver chaves key1 em event[]
    s = event['key1']

    body=[
        {
            'data_hora': data_hora,
            'msg': s
        }
    ]

    return {
    # Sucesso
        'statusCode': 200,
        'body': json.dumps(body)
    }
