import psutil

def info_rede():
    """
    Função para verificar conectividade com a rede

    Returns: True caso tenha rede e False caso contrário
    """

    # Captura de rede
    rede = psutil.net_io_counters()

    # Upload
    upload = round(rede.bytes_sent / (1024 ** 2), 2)

    # Download
    download = round(rede.bytes_recv / (1024 ** 2), 2)

    # Informações
    info = {
        "upload": upload,
        "download": download
    }

    return info

