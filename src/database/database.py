import os, colorama
import mysql.connector
from mysql.connector import Error
from colorama import Fore, Style, init
init()

def conectar():

    # Configurações de acesso
    config = {
        'hostname': os.getenv('DB_HOSTNAME'),
        'database': os.getenv('DB_DATABASE'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'port': os.getenv('DB_PORT')
    }

    try:
        # Tenta estabelecer a conexão com o banco
        conexao = mysql.connector.connect(**config)

        if conexao.is_connected():
            print("Conexão com o banco de dados estabelecida!")
            return conexao

    except Error as erro:
        # Erros comuns
        if erro.errno == 1045:
            print(Fore.RED + "Erro: Usuário ou senha incorretos." + Style.RESET_ALL)
        elif erro.errno == 1049:
            print(Fore.RED + "Erro: O banco de dados especificado não existe." + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Erro de banco de dados: {erro}" + Style.RESET_ALL)
        return None
    except Exception as erro:
        print(Fore.RED + f"Erro inesperado: {erro}" + Style.RESET_ALL)
        return None


