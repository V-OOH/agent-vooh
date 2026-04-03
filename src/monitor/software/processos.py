import psutil

def capturar_processos(intervalo: int) -> list[dict[str, str]] | None:
    """
    Captura informações detalhadas dos processos do sistema.

    Returns:
        Uma lista de dicionários com os processos
    """

    # Items dos processos
    processos = psutil.process_iter(['username', 'name', 'pid', 'status', 'memory_info', 'cpu_percent'])

    # Lista de processos
    lista_processos = []

    # Percorre a lista de processos
    for processo in processos:

        # Chave de acesso ao processo
        p = processo.info

        # Valida se não tem usuário informado
        usuario = p['username'].split('\\')[0] if p['username'] else "Sistema"

        # Dados do processo
        info = {
            "pid": p['pid'],
            "usuario": usuario,
            "nome": p['name'],
            "status": p['status'],
            "memoria": p['memory_info'].rss,
            "uso_cpu": p['cpu_percent']
        }

        # Adiciona os processos na lista de processos
        lista_processos.append(info)

    return lista_processos if lista_processos else None
   