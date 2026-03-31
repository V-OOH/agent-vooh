import psutil

def info_ram() -> dict:
    """
    Função para detectar capacidade de RAM do dispositivo

    Returns: Dicionário de informações da RAM
    """

    # Objeto de RAM do psutil
    ram = psutil.virtual_memory()

    # Razão de conversão
    razao = 1 / (1024 ** 3)

    # RAM total
    total = ram.total * razao

    # RAM disponível
    disponivel = ram.available * razao

    # RAM em uso (%)
    percentual = ram.percent

    # Informações da RAM
    info = {
        "total": total,
        "disponivel": disponivel,
        "percentual": percentual
    }

    # Retorna as informações
    return info