import psutil, socket, colorama, time, subprocess, platform
from colorama import Fore, Style

def get_ping():
    host = "8.8.8.8"
    param = "-n" if platform.system().lower() == "windows" else "-c"
    comando = ["ping", param, "1", host]
    
    try:
        saida = subprocess.check_output(comando, stderr=subprocess.STDOUT, text=True)
       
        if "tempo=" in saida: 
            return float(saida.split("tempo=")[1].split("ms")[0])
        elif "time=" in saida: 
            return float(saida.split("time=")[1].split(" ms")[0])
    except:
        return 0.0
    return 0.0


def info_rede()-> dict[str, str]:
    """
    Função para verificar conectividade com a rede

    Returns: True caso tenha rede e False caso contrário
    """

    # Captura de rede
    rede = psutil.net_io_counters()

    # Mac e IP da máquina
    i = info_mac_ip_address()

    # Upload
    upload = rede.bytes_sent

    # Download
    download = rede.bytes_recv
    
    # Interfaces
    interfaces = psutil.net_if_addrs()
    nome_interface = None
    for nome, addrs in interfaces.items():
        if any(addr.address == i['ip'] for addr in addrs):
            nome_interface = nome
            break

    # Erros de I/O
    io_counters = psutil.net_io_counters(pernic=True)

    #Status da rede
    status_rede = io_counters.get(nome_interface)

    #MTU e Velocidade
    if_status = psutil.net_if_stats().get(nome_interface)

    #Tipo de conexão      inet - filtra conexões IPV4 e IPV6
    conexoes = psutil.net_connections(kind='inet')
    estados = [c.status for c in conexoes]

    todas_interfaces = []
    for nome, stats in io_counters.items():
        if_st = psutil.net_if_stats().get(nome)
        todas_interfaces.append({
            "nome":       nome,
            "upload":     stats.bytes_sent,
            "download":   stats.bytes_recv,
            "dropin":     stats.dropin,
            "dropout":    stats.dropout,
            "errin":      stats.errin,
            "errout":     stats.errout,
            "mtu":        if_st.mtu   if if_st else 0,
            "ativa":      if_st.isup  if if_st else False,
            "velocidade": if_st.speed if if_st else 0,
        })

    # Informações
    info = {
        "ip": i['ip'],
        "mac": i['mac'],
        "upload": status_rede.bytes_sent if status_rede else 0,
        "download": status_rede.bytes_recv if status_rede else 0,
        "errin": status_rede.errin if status_rede else 0,
        "dropin": status_rede.dropin if status_rede else 0,
        "mtu": if_status.mtu if if_status else 0,
        "latencia": get_ping(),
        "conn_established": estados.count('ESTABLISHED'),
        "conn_listen": estados.count('LISTEN'),
        "conn_time_wait": estados.count('TIME_WAIT'),
        "conn_close_wait": estados.count('CLOSE_WAIT'),
        "conn_syn_sent": estados.count('SYN_SENT'),
        "interfaces": todas_interfaces,
    }

    return info

def info_mac_ip_address()-> dict[str, str] | None:
    """
    Retorna o IP e o MacAddress

    Returns: Dicionário de informações da placa de rede

    """
    # Realiza uma chamada de conexão via socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Tenta se conectar ao IP público do Goolgle
        s.connect(("8.8.8.8", 80))
        ip1 = s.getsockname()[0]
    except Exception as erro:
        print("Ocorreu um erro:" + str(erro))

    # Lista as interfaces de IP
    interfaces = psutil.net_if_addrs()

    # IP e Mac
    ip_mac = {}

    # Percorre a lista de interfaces e endereços
    for nome_interface, addrs in interfaces.items():
        ip = None
        mac = None

        for addr in addrs:
            if addr.family == socket.AF_INET:
                ip = addr.address
            elif addr.family == psutil.AF_LINK:
                mac = addr.address

        if ip1 == ip:

            ip_mac = {
                "ip": ip,
                "mac": mac
            }

            return ip_mac

    return None
