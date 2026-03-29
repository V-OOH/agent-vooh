import platform, subprocess, sys, psutil

from colorama import Fore

def processador(plataforma: str) -> dict:
    """
    Obtém informações detalhadas do processador

    Returns: Dicionário de informações do processador
    """

    # Valor inicial do nome da CPU
    cpu_nome = "Desconhecido"

    # Tenta detectar informações do processador
    try:
        if plataforma == "Linux":
            comando = subprocess.run(
                "cat /proc/cpuinfo | grep 'model name' | head -n 1",
                shell=True,
                capture_output=True,
                text=True
            )

            cpu_nome = comando.stdout.split(":")[1].strip()

        elif plataforma == "Windows":
            comando = subprocess.run(
                "wmic cpu get name",
                shell=True,
                capture_output=True,
                text=True
            )
            cpu_nome = comando.stdout.split("=")[1].strip()

        else:
            print(Fore.RED + "Erro: Plataforma não suportada!")
            sys.exit(1)
    except Exception as excecao:
        print(Fore.RED + f"Falha ao obter informaçõesda CPU: {excecao}")

    # Quantidade de núcleos físicos
    nucleos = psutil.cpu_count(logical=False)

    # Quantidade de núcleos lógicos e físicos
    nucleos_total = psutil.cpu_count()

    # Obtém a frequência da CPU
    freq = psutil.cpu_freq()

    # Frequência máxima
    freq_max = str(freq.max)

    # Frequência mínima
    freq_min = str(freq.min)

    # Dicionário de informaçõe
    informacoes_processador = {
        "processador": cpu_nome,
        "nucleos_fisicos": nucleos,
        "nucleos_totais": nucleos_total,
        "frequencia_min": freq_min,
        "frequencia_max": freq_max,
    }

    # Retorna as informações
    return informacoes_processador