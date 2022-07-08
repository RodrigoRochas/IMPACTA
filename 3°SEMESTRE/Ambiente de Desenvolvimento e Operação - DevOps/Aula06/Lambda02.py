import json
from datetime import datetime
import urllib.parse
import boto3

# Conexão com o S3
s = boto3.client('s3')


def lambda_handler(event, context):
    # Data e hora para registrar na mensagem
    data_hora = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    # Dados da mensagem vindos via HTTP POST
    # Deve haver chaves key1 em event[]
    x = event['key1']

    # O try/catch é para erro no acesso ao S3
    try:
        # A role deve ser configurada para a esta função,
        # permitindo PutItem para S3
        fname = "a.txt"
        f = open('/tmp/' + fname, 'w')
        f.write(x)
        f.close()
        s.upload_file('/tmp/' + fname, 'bucketgoya1', fname)

        return {
        # Sucesso
            'statusCode': 200,
            'body': json.dumps('Arquivo inserida no S3')
        }

    except:
        # Erro: Imprime mensagem de erro no log da função lambda
        # print('Erro: lambda function terminada sem sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao inserir em S3')
        }
