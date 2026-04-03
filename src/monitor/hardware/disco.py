import sys, psutil

def info_disco(plataforma: str) -> list[dict[str, str]]:
    """
    Faz a captura de dados do disco

    Args:
        plataforma (str): Windows ou Linux

    Returns:
        Dicionário de informações do disco:

            - Total do disco em bytes

            - Total usado do disco em bytes

            - Total livre do disco em bytes

            - Percentual de uso do disco
    """

    # Root do sistema
    root = ""

    # Lista de discos
    lista_disco = []

    if plataforma == "Linux":
        root = "/"
    elif plataforma == "Windows":
        root = "C:\\"
    else:
        print("Plataforma não suportada: " + plataforma)
        sys.exit(1)

    # Objeto de disco
    disco = psutil.disk_usage(root)

    # Dados
    dados = {
        "total": disco.total,
        "usado": disco.used,
        "livre": disco.free,
        "percentual": disco.percent
    }

    # Adiciona na lista de informações do disco os dados
    lista_disco.append(dados)

    # Retorna a lista
    return lista_disco