# Importações
import time

import sys
from colorama import Fore, Style, init

from src.monitor.hardware.disco import info_disco
from src.monitor.software.info import informacoes
from src.monitor.hardware.processador import info_processador
from src.monitor.hardware.ram import info_ram
from src.database.database import buscar_id_display

# Inicializa o colorama
init()

# Função para obter informações do sistema
def identificar(plataforma: str) -> str | None:
    """
    Faz a detecção inicial de informações do dispositivo

    Args:
        plataforma: Windows ou Linux
    """

    # Aviso de detecção do dispositivo
    print(Fore.MAGENTA + "\nDetectando dispositivo\n" + Style.RESET_ALL)

    # Aviso de detectando informações de software
    print(Fore.MAGENTA + "✱ Lendo informações de software...\n" + Style.RESET_ALL)

    # Aguarda 3 segundos
    time.sleep(3)

    # Informações de software
    so = informacoes()

    # Exibe as informações do sistema
    print(Fore.GREEN + "Plataforma: " + Style.RESET_ALL + so['sistema'] + Fore.GREEN + " ✓" + Style.RESET_ALL)
    print(Fore.GREEN + "Kernel: " + Style.RESET_ALL + so['kernel'] + Fore.GREEN + " ✓" + Style.RESET_ALL)
    print(Fore.GREEN + "Versão do kernel: " + Style.RESET_ALL + so['versao'] + Fore.GREEN + " ✓" + Style.RESET_ALL)
    print(Fore.GREEN + "Host: " + Style.RESET_ALL + so['host'] + Fore.GREEN + " ✓" + Style.RESET_ALL)
    print(Fore.GREEN + "Usuário: " + Style.RESET_ALL + so['usuario'] + Fore.GREEN + " ✓" + Style.RESET_ALL)

    # Aviso de detectando informações de hardware
    print(Fore.MAGENTA + "\n✱ Lendo informações de hardware...\n" + Style.RESET_ALL)

    # Aguarda 4 segundos
    time.sleep(4)

    # Informações de hardware
    proc = info_processador(plataforma)

    # Exibe as informações do processador
    print(Fore.GREEN + "Processador: " + Style.RESET_ALL + proc['processador'])
    print(Fore.GREEN + "     ➔ Quantidade de núcleos: " + Style.RESET_ALL + str(proc['nucleos_totais']))
    print(Fore.GREEN + "     ➔ Núcleos físicos: " + Style.RESET_ALL + str(proc['nucleos_fisicos']))
    print(Fore.GREEN + "     ➔ Núcleos totais: " + Style.RESET_ALL + str(proc['nucleos_totais']))
    print(Fore.GREEN + "     ➔ Frequência mínima: " + Style.RESET_ALL + str(proc['frequencia_min']) + " Mhz")
    print(Fore.GREEN + "     ➔ Frequência máxima: " + Style.RESET_ALL + str(proc['frequencia_max']) + " Mhz")

    # Informações da RAM
    ram = info_ram()

    # Exibe as informações da RAM
    print(Fore.GREEN + "Capacidade de RAM: " + Style.RESET_ALL + str(round(float(ram['total'] / 1024 ** 3), 2)) + " GiB")
    print(Fore.GREEN + "     ➔ Disponível: " + Style.RESET_ALL + str(round(float(ram['disponivel'] / 1024 ** 3), 2)) + " GiB")
    print(Fore.GREEN + "     ➔ Usado: " + Style.RESET_ALL + str(round(ram['percentual'], 2)) + "%")

    # Informações do Disco
    disco = info_disco(plataforma)

    # Exibe as informações do disco
    print(Fore.GREEN + "Capacidade do disco: " + Style.RESET_ALL + f"{round((float(disco[0]['total']) / 1024 ** 3), 2)} GiB")
    print(Fore.GREEN + "     ➔ Disponível: " + Style.RESET_ALL + f"{round((float(disco[0]['usado']) / 1024 ** 3), 2)} GiB")
    print(Fore.GREEN + "     ➔ Usado: " + Style.RESET_ALL + f"{round(float(disco[0]['percentual']))}%\n")

    print(Fore.YELLOW + f"Obtendo o registro do equipamento..." + Style.RESET_ALL)

    # Faz a busca do ID do display cadastrado
    display = buscar_id_display("a4:63:a1:6e:67:09")

    if display:
        return display['id']
    else:
        print(Fore.RED + "Não é possível associar um registro neste equipamento!" + Style.RESET_ALL)
    return None