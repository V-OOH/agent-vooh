import logging
import time

import boto3
from botocore.exceptions import ClientError
import os
from colorama import Fore, Style
from dotenv import load_dotenv



s3.upload_file('data/dados.csv', 'vooh-bucket', 'raw/dados.csv')
s3.upload_file('data/processos.csv', 'vooh-bucket', 'raw/processos.csv')
print("Upload concluído com sucesso!")


def upload_file(arquivo, bucket, nome_objeto=None):
    """
    Faz upload de um arquivo para um bucket na S3

    Args:
        arquivo: File to upload
        bucket: Bucket para upload
        nome_objeto: É o nome único e o caminho completo que um arquivo receberá após o upload

    Returns:
        True se o arquivo foi enviado, senão False
    """

    # Carrega as credenciais do .env
    load_dotenv()

    # Valida se o nome do objeto é nulo e atribui
    if nome_objeto is None:
        nome_objeto = os.path.basename(arquivo)

    # Faz o upload do arquivo usando as credenciais do .env
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        aws_session_token=os.getenv('AWS_SESSION_TOKEN')
    )

    # Tenta fazer o upload do arquivo
    try:
        # Resposta do envio
        response = s3_client.upload_file(arquivo, bucket, nome_objeto)

        if response:
            print(Fore.GREEN + f"[{time.strftime("%d-%m-%Y %H-%M-%S")}] - Sucesso: Arquivo {arquivo} enviado!")

    except ClientError as erro:
        logging.error(erro)
        print(Fore.RED + "Ocorreu um erro: " + f"{erro}" + Style.RESET_ALL)
        return False
    return True