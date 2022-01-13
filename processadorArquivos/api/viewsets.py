from rest_framework import viewsets, status
from rest_framework.response import Response

import pandas as pd


class ArquivoViewSet(viewsets.ViewSet):
    # Permitir apenas métodos post
    http_method_names = ['post']

    def create(self, request):
        arquivo = request.data.get('arquivo')
        # Verificações do arquivo, se enviou algo com a chave arquivo
        if arquivo is None:
            return Response(status=status.HTTP_204_NO_CONTENT)

        # Abrir o arquivo utilizando a biblioteca pandas e caso dê algum erro retornar uma mensagem e o status 400
        try:
            df = pd.read_csv(arquivo, delimiter=';')

        except FileNotFoundError:
            return Response("Arquivo não encontrado", status=status.HTTP_400_BAD_REQUEST)

        except pd.errors.EmptyDataError:
            return Response("Arquivo vazio", status=status.HTTP_400_BAD_REQUEST)

        except Exception:
            return Response("Outras Exceções", status=status.HTTP_400_BAD_REQUEST)

        # Definimos um dicionario com a chave valores e cujo valor atribuido é uma lista com
        # os valores extraídos do dataframe

        resposta = {
            "valores": df.values
        }

        print(df.values)

        # Retornamos o dicionário resposta para quem chamou a aplicação
        return Response(resposta, status=200)
