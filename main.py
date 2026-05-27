# Importações
import platform
import sys

from colorama import Fore, Style, init

from src.capturar import captura
from src.detectar import identificar

# Inicializa o colorama
init()

# VOOH ASCII Arte
print(
    Fore.MAGENTA
    + """
██     ██  ███████   ███████  ██     ██ 
██     ██ ██     ██ ██     ██ ██     ██ 
██     ██ ██     ██ ██     ██ ██     ██ 
██     ██ ██     ██ ██     ██ █████████ 
 ██   ██  ██     ██ ██     ██ ██     ██ 
  ██ ██   ██     ██ ██     ██ ██     ██ 
   ███     ███████   ███████  ██     ██ 
"""
    + Style.RESET_ALL
)

# Informações de copyright
print(
    Fore.GREEN
    + "© COPYRIGHT 2026 · VOOH - MONITORAMENTO DE DOOH · TODOS OS DIREITOS RESERVADOS."
    + Style.RESET_ALL
)

# Obtém os argumentos
argumentos = sys.argv

# Frequência padrão em segundos
FREQ_PADRAO = 30

# Plataforma
plataforma = platform.system()

# Valida se há argumentos
if len(argumentos) == 1:
    print(
        Fore.YELLOW
        + "\nOs argumentos não foram passados. Executando no modo padrão."
        + Style.RESET_ALL
    )

    frequencia = FREQ_PADRAO

# Valida se há 1 argumento (recurso passado)
if len(argumentos) > 1:
    # Frequência de captura dos dados
    frequencia = int(argumentos[1])

    if frequencia <= 0 or frequencia > 18000:
        print(
            Fore.RED
            + "Erro: Valor não pode ser negativo ou superior a 18.000 segundos (5h)"
            + Style.RESET_ALL
        )
        sys.exit(1)
    else:
        try:
            # Identificar informações da máquina
            i = identificar(plataforma=plataforma)

            if i is not None:
                dados_equipamento = {
                    "id_display": i["id"],
                    "id_empresa": i["id_empresa"],
                    "id_zona": i["id_zona"],
                }

                print("\n")

                captura(
                    frequencia=frequencia,
                    plataforma=plataforma,
                    dados_equipamento=dados_equipamento,
                )
            else:
                print(
                    Fore.RED
                    + "Não foi possível vincular registro do equipamento"
                    + Style.RESET_ALL
                )

        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n\nInterrompendo..." + Style.RESET_ALL)
            sys.exit(0)


# Valida se há mais de 2 argumentos (não suportado)
if len(argumentos) > 2:
    print(Fore.RED + "Erro: Argumentos execessivos!" + Style.RESET_ALL)
    print(
        Fore.YELLOW + "\nForma de uso: python3 main.py [frequência]" + Style.RESET_ALL
    )
    sys.exit(1)
