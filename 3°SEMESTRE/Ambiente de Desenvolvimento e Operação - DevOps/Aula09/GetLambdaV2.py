'''
Esta função foi escrita para ser acessada via HTTP POST (REST)
através de um API Gateway:
  - Solicitação de Integração: Lambda, sem proxy
  - Solicitação de método: Auth=None
  - Com ativação de CORS
'''


import json
from datetime import datetime
import boto3


# Os dois comandos abaixo estao fora do handler para melhor performance
# Conexão com o Banco de Dados DynamoDB
dynamodb = boto3.resource('dynamodb')

# Conexão com a Tabela de Lances
# Deve haver uma tabela com o nome "LancesDaAlexia":
# Com chave de partition: 'user'
# Chave de ordenação: 'data_hora'
tableLances = dynamodb.Table('LancesDaAlexia')


def lambda_handler(event, context):
    # Data e hora para registrar na mensagem
    data_hora = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    # Dados da mensagem vindos via HTTP POST
    # As chaves de event[] devem bater com os ids do formulário
    usuario = str(event['from'])
    lance = str(event['bid'])

    # O try/catch é para erro no acesso ao DynamoDB
    try:
        # Uma role deve ser configurada para a esta função,
        # permitindo PutItem para DynamoDB
        dia="quarta-feira"
        tableLances.put_item(
            Item={
                'user': usuario, # Chave de Partição  no Banco
                'data_hora': data_hora, # Chave de Ordenação no Banco
                'dia_da_semana': dia,
                'bid': lance
            }
        )

        return {
        # Sucesso
            'statusCode': 200,
            'body': json.dumps('Lance de '
                               + usuario
                               + ' no valor '
                               + lance
                               + ' inserida no Banco de Dados')
        }

    except:
        # Erro: print() coloca mensagem de erro no log da função lambda
        print('Erro: LambdaDoJonas terminada sem sucesso')
        return {
            'statusCode': 400,
            'body': json.dumps('Erro ao tentar processar mensagem')
        }
