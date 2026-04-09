import time, psutil, sys, colorama

from colorama import Fore, Style
from src.monitor.hardware.disco import info_disco
from src.monitor.hardware.processador import info_processador
from src.monitor.hardware.ram import info_ram
from src.monitor.hardware.rede import info_rede
from src.util.salvar import salvar
from src.monitor.software.processos import capturar_processos

# Captura os dados com base num componente e numa frequência
def captura(frequencia: int, plataforma: str):
    """
    Faz a captura de dados de um componente de hardware da máquina

    Args:
        frequencia: O valor da frequência.
        plataforma: Windows ou Linux
    """

    print(Fore.MAGENTA + f"Iniciando a captura de dados a cada {frequencia}s" + Style.RESET_ALL)

    print(Fore.CYAN + "\nExecutando ..." + Style.RESET_ALL)

    # Plataformas suportadas
    plataforma_suportadas = ["Windows", "Linux"]

    if plataforma not in plataforma_suportadas:
        print("Plataforma não suportada")
        sys.exit()

    # Loop
    while True:

        # Informações do disco
        disco = info_disco(plataforma=plataforma)
        d = disco[0]

        # Capacidade total do disco
        total_disco = d["total"]

        # Total usado do disco
        disco_usado = d["usado"]

        # Quantiadade de armazenamento livre do disco
        disco_livre = d["livre"]

        # Uso em percentual do disco
        disco_percentual = d["percentual"]

        # Informações do processador
        processdor = info_processador(plataforma=plataforma)
        p = processdor

        # Nome e modelo do processador
        processador_nome = p["processador"]

        # Quantidade de núcleos físicos do processador
        nucleos_fisicos = p["nucleos_fisicos"]

        # Núcleos totais do processador
        nucleos_totais = p["nucleos_totais"]

        # Frequência mínima do processador
        frequencia_min = p["frequencia_min"]

        # Frequência máxima do processador
        frequencia_max = p["frequencia_max"]

        # Frequência atual do processador
        frequencia_atual = p["frequencia_atual"]

        # Percentual de uso da CPU
        cpu_percentual = p["percentual"]

        # Informações da memória RAM
        ram = info_ram()
        r = ram

        # Capacidade total da RAM
        ram_total = r["total"]

        # RAM total disponível
        ram_disponivel = r["disponivel"]

        # Percentual de uso da RAM
        ram_percentual = r["percentual"]

        # Informações da Rede
        rede = info_rede()
        n = rede

        # Bytes de upload
        upload = n["upload"]

        # Bytes de download
        download= n["download"]

        # MacAdress
        mac = n["mac"]

        # IP
        ip = n['ip']

        # Cabeçalhos (Campos)
        cabecalho = [
            "data_hora",
            "total_disco",
            "disco_usado",
            "disco_livre",
            "disco_percentual",
            "processador_nome",
            "nucleos_fiscos",
            "nucleos_totais",
            "frequencia_min",
            "frequencia_max",
            "frequencia_atual",
            "cpu_percentual",
            "ram_total",
            "ram_disponivel",
            "ram_percentual",
            "upload",
            "download",
            "mac",
            "ip"
        ]

        # Dicionários de dados da leitura
        dados = {
            "data_hora":time.strftime('%d-%m-%Y %H:%M:%S'),
            "total_disco": total_disco,
            "disco_usado": disco_usado,
            "disco_livre": disco_livre,
            "disco_percentual": disco_percentual,
            "processador_nome": processador_nome,
            "nucleos_fiscos": nucleos_fisicos,
            "nucleos_totais": nucleos_totais,
            "frequencia_min": frequencia_min,
            "frequencia_max": frequencia_max,
            "frequencia_atual": frequencia_atual,
            "cpu_percentual": cpu_percentual,
            "ram_total": ram_total,
            "ram_disponivel": ram_disponivel,
            "ram_percentual": ram_percentual,
            "upload": upload,
            "download": download,
            "mac": mac,
            "ip": ip
        }

        # Captura os processos
        processos = capturar_processos(intervalo=frequencia)

        for p in processos:

            # Cabeçalho dos processos
            head = [
                "data_hora",
                "pid",
                "usuario",
                "nome",
                "status",
                "memoria",
                "uso_cpu",
                "mac",
                "ip"
            ]

            # Processos
            proc = {
                "data_hora": time.strftime("%d-%m-%Y %H:%M:%S"),
                "pid": p['pid'],
                "usuario": p['usuario'],
                "nome": p['nome'],
                "status": p['status'],
                "memoria": p['memoria'],
                "uso_cpu": p['uso_cpu'],
                "mac": mac,
                "ip": ip
            }

            # Salva apenas processos com uso de CPU > 0
            if float(p['uso_cpu']) > 0:
                # Salva os dados ds procesos
                salvar(arquivo="data/processos.csv", campos=head, dados=proc)

        # Salva os dados em data/dados.csv
        salvar(arquivo="data/dados.csv", campos=cabecalho, dados=dados)

        # Intervalo de captura e salvamento de dados
        time.sleep(frequencia)