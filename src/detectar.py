# Importações
from colorama import Fore, Style, init

from helper.software import software

# Inicializa o colorama
init()

# Função para obter informações do sistema
def detectar():
    """
    Faz a detecção de informações do dispositivo

    Returns:
        Lista de informações do dispositivo
    """

    # Aviso de detecção do dispositivo
    print(Fore.MAGENTA + "Detectando dispositivo..." + Style.RESET_ALL)

    # Informações de software
    info_software = software()

    # Informações de hardware
    # info_hardware = hardware()

    print(info_software)



