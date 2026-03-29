# Importações
import time

from colorama import Fore, Style, init
from src.monitor.software.info import informacoes

# Inicializa o colorama
init()

# Função para obter informações do sistema
def sistema():
    """
    Faz a detecção de informações do dispositivo

    Returns:
        Lista de informações do dispositivo
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