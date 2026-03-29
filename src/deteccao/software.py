import platform, getpass

def software() -> dict[str, str]:
    """
    Função para detectar as informações de software do dispositivo

    Obtém as informações de:
        - Sistema (Linux ou Windows)
        - Kernel
        - Versão do kernel
        - Host (Nome de máquina)
        - Usuário

    Returns: Dicionário de informações do software
    """

    # Informações do sistema (Linux ou Windows)
    sistema = platform.system()

    # Informações do Kernel
    kernel = platform.release()

    # Versão do Kernel
    versao = platform.version()

    # Host
    host = platform.node()

    # Usuário
    usuario = getpass.getuser()

    # Dicionário de informações
    informacoes = {
        "sistema" : sistema,
        "kernel": kernel,
        "versao": versao,
        "host": host,
        "usuario": usuario
    }

    # Retorna as informações obtidas
    return informacoes
