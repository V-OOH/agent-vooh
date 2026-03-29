import platform, subprocess, sys, psutil

from colorama import Fore

def processador(plataforma: str) -> dict[str, str]:
    """
    Obtém informações do processador

    Returns: Dicionário de informações do processador
    """

    if plataforma == "Linux":
        comando = subprocess.run(
            "cat /proc/cpuinfo | grep 'model name' | head -n 1",
            shell=True,
            capture_output=True,
            text=True
        )
        comando.stdout.split(":")[1].strip()
        cpu = comando

    elif plataforma == "Windows":
        comando = subprocess.run(
            "wmic cpu get name",
            shell=True,
            capture_output=True,
            text=True
        )
        comando.stdout.split("=")[1].strip()
        cpu = comando

    else:
        print(Fore.RED + "Erro: Plataforma não suportada!")
        sys.exit(1)

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
    informacoes = {
        "processador": cpu,
        "nucleos_fisicos": nucleos,
        "nucleos_totais": nucleos_total,
        "frequencia_min": freq_min,
        "frequencia_max": freq_max,
    }

    # Retorna as informações
    return informacoes