import psutil

def capturar_processos(intervalo: int, info=None) ->dict:
    """
    Função para capturar processos

    Returns:

    """

    processos = psutil.process_iter(['username', 'name', 'pid', 'status', 'memory_info', 'cpu_percent'])

    # Percorre a lista de processos
    for processo in processos:

        # Chave de acesso ao processo
        p = processo.info

        # Usuário
        usuario = p['username']

        # Valida se não tem usuário informado
        if p['username'] is not None:
            # Traz somente o usuario sem o dominio
            usuario = p['username'].split('\\')[0]
        else:
            usuario = "Sistema"

        # Uso de memoria do processo
        memoria = p['memory_info'].rss # RSS = Resident Set Size - o quanto está ocupando na RAM naquele momento

        # Memória em MB
        mem = memoria / (1024 ** 2)

        # PID
        pid = p['pid']

        # Uso de CPU
        uso_cpu = uso_cpu_por_processo(pid)

        # Status
        status = p['status']

        # Nome do processo
        nome = p['name']

        # Informações
        info = {
            "pid": pid,
            "usuario": usuario,
            "nome": nome,
            "status": status,
            "memoria": mem,
            "uso_cpu": uso_cpu
        }
    return info

def uso_cpu_por_processo(pid: int) -> float:

    processos = psutil.Process(31821)
    nucleos = psutil.cpu_count(logical=True)

    p = processos
    uso = p.cpu_percent(interval=5) / nucleos

    return uso

    
   