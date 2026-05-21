import os
import sys
from typing import Any

import mysql.connector
from colorama import Fore, Style, init
from mysql.connector import Error

init()

def conectar():
    """
    Realiza a conexão com o banco de dados

    Returns: Conexão com o banco de dados

    """

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


def buscar_id_display(mac_address: str) -> dict[str, Any] | None:
    """
    Retorna o ID do equipamento registrado no banco de dados

    Args:
        mac_address: Endereço MAC do equipamento

    Returns:
        Dicionário com o ID do equipamento
    """

    sql = f"""
    SELECT id, identificacao FROM display
    WHERE mac = %s
    """

    conexao = conectar()

    if conexao:
        try:
            cursor = conexao.cursor(dictionary=True)

            cursor.execute(sql, mac_address)

            resultado = cursor.fetchall()

            if resultado is None:
                print(Fore.RED + "Erro ao validar o ID do equipamento. Tente novamente mais tarde." + Style.RESET_ALL)
                sys.exit(0)
            else:
                dados = {
                    "id": resultado['id'],
                    "mac": resultado['mac']
                }

            return dados
        except Error as erro:
            print(Fore.RED + f"Erro: {erro}" + Style.RESET_ALL)
            conexao.rollback()
        finally:
            cursor.close()
            conexao.close()
            print(Fore.BLUE + "Conexão com banco de dados encerrada" + Style.RESET_ALL)
    return None
