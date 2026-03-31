import psutil

def info_disco(plataforma: str) -> dict:
    """
    Função para ler dtalhadamente os dados do disco.

    Args:
        plataforma (str): Windows ou Linux

    Returns: Dicionário de informações do disco
    """

    root = ""

    if plataforma == "Linux":
        root = "/"
    elif plataforma == "Windows":
        root = "C:\\"

    # Objeto de disco do psutil
    disco = psutil.disk_usage(root)

    #

    # Informações do disco
    info = {

    }


    return info