# Importações
import platform, sys, colorama
import time

from colorama import Fore, Style, init

# Inicializa o colorama
init()

# VOOH ASCII Arte
print(Fore.MAGENTA + """
██     ██  ███████   ███████  ██     ██ 
██     ██ ██     ██ ██     ██ ██     ██ 
██     ██ ██     ██ ██     ██ ██     ██ 
██     ██ ██     ██ ██     ██ █████████ 
 ██   ██  ██     ██ ██     ██ ██     ██ 
  ██ ██   ██     ██ ██     ██ ██     ██ 
   ███     ███████   ███████  ██     ██ 
""" + Style.RESET_ALL)

# Informações de copyright
print(Fore.GREEN + "© COPYRIGHT 2026 · VOOH - MONITORAMENTO DE DOOH · TODOS OS DIREITOS RESERVADOS." + Style.RESET_ALL)

# Obtém os argumentos
argumentos = sys.argv

# Recursos disponíveis
recursos = ["-c", "-r", "-n", "-d", "-p", "-t", "--all"]

# Frequência padrão em segundos
FREQ_PADRAO = 30

# Valida se há argumentos
if len(argumentos) == 1:
    print(Fore.YELLOW + "\nOs argumentos não foram passados. Executando no modo padrão." + Style.RESET_ALL)
    recurso = "--all"

# Valida se há 1 argumento (recurso passado)
elif len(argumentos) == 2:

    # Recurso a ser monitorado
    recursos = argumentos[1]

    # Frequência de captura dos dados
    frequencia = FREQ_PADRAO

    # Valida se o recurso informado é válido
    if argumentos[1] not in recursos:
        print(Fore.RED + "\nErro: Recurso inválido!" + Style.RESET_ALL)
        print(f"\nRecursos disponíveis: \n-c     CPU\n-r     RAM\n-n     Rede\n-d     Disco\n-p     Processos\n-t     Temperatura\n--all  Todos os recursos")
        sys.exit(1)

# Valida se há mais de 1 argumento (recurso e frequência passado)
elif len(argumentos) == 3:

    # Recuros a ser monitorado
    recurso = argumentos[1]

    # Frequência de captura dos dados
    frequencia = int(argumentos[2])

    # Valida se o recurso informado é válido
    if argumentos[1] not in recursos:
        print(Fore.RED + "\nErro: Recurso inválido!" + Style.RESET_ALL)
        print(f"\nRecursos disponíveis: \n-c CPU\n-r RAM\n-n Rede\n-d Disco\n-p Processos\n-t Temperatura\n--all Todos os recursos")
        sys.exit(1)

    # Valida se o número passado é válido
    elif frequencia <= 0 or frequencia > 18000:
        print(Fore.RED + "Erro: Valor não pode ser negativo ou superior a 18.000 segundos (5h)" + Style.RESET_ALL)
        sys.exit(1)

    # Valida se há mais de 2 argumentos (não suportado)
    elif len(argumentos) > 3:
        print(Fore.RED + "Erro: Argumentos execessivos!" + Style.RESET_ALL)
        print(Fore.YELLOW + "\nForma de uso: python3 main.py [recurso] [frequência]" + Style.RESET_ALL)
        sys.exit(1)

    # Caso não tenha erros
    else:
        try:
            while True:
                print("Detectando Hardware")
                time.sleep(10)

        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n\nInterrompendo..." + Style.RESET_ALL)
            sys.exit(0)