import os
import sys
from pathlib import Path
from typing import Any

import dotenv
import mysql.connector
from colorama import Fore, Style, init
from mysql.connector import Error

def conectar():
    """
    Realiza a conexão com o banco de dados

    Returns: Conexão com o banco de dados

    """

    env_path = Path(__file__).resolve().parent.parent.parent / '.env'
    dotenv.load_dotenv(env_path)

    # Configurações de acesso
    config = {
        'host': os.getenv('DB_HOSTNAME'),
        'database': os.getenv('DB_DATABASE'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'port': os.getenv('DB_PORT')
    }


    try:
        for var, valor in config.items():
            if valor is None:
                print(Fore.RED + f"Erro: Variável {var} não definida!" + Style.RESET_ALL)
                sys.exit(0)

        # Tenta estabelecer a conexão com o banco
        conexao = mysql.connector.connect(**config)

        if conexao.is_connected():
            print(Fore.GREEN +  f"Conexão com o banco de dados estabelecida!" +  Style.RESET_ALL)
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


def buscar_id_display(mac_address: str) -> dict[str, Any] | None:
    """
    Retorna o ID do equipamento registrado no banco de dados

    Args:
        mac_address: Endereço MAC do equipamento

    Returns:
        Dicionário com o ID do equipamento
    """

    sql = """
    SELECT 
        d.id AS 'id_display',
        d.mac AS 'mac_display',
        e.id AS 'id_empresa'
    FROM display AS d
    INNER JOIN empresa AS e 
    ON d.fk_empresa = e.id
    WHERE d.mac = %s
    """

    conexao = conectar()

    if conexao:
        try:
            cursor = conexao.cursor(dictionary=True)

            cursor.execute(sql, (mac_address,))

            resultado = cursor.fetchone()

            if resultado is None:
                print(Fore.RED + "Erro: Equipamento não cadastrado." + Style.RESET_ALL)
                sys.exit(0)
            else:
                dados = {
                    "id_display": resultado['id_display'],
                    "mac_display": resultado['mac_display'],
                    "id_empresa": resultado['id_empresa']
                }

            return dados
        except Error as erro:
            print(Fore.RED + f"Erro: {erro}" + Style.RESET_ALL)
            conexao.rollback()
        finally:
            cursor.close()
            conexao.close()
            print(Fore.BLUE + "Conexão com o banco de dados encerrada!" + Style.RESET_ALL)
    return None
