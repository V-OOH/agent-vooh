import psutil
import subprocess
from colorama import Fore, Style


def info_temperatura(plataforma: str) -> dict[str, float | None]:
    """
    Obtém informações da temperatura padronizadas por plataforma.
    """
    try:
        if plataforma == "Linux":
            # Captura o retorno da função do Linux
            return get_temp_linux()
        elif plataforma == "Windows":
            # Captura o retorno da função do Windows
            return get_temp_windows()
        else:
            return {}
    except Exception as erro:
        return {}


def get_temp_windows() -> dict[str, float | None]:
    """
    Obtém a temperatura no Windows via PowerShell (CIM).
    Requer execução como Administrador.
    """
    cmd = "(Get-CimInstance -Namespace root/wmi -ClassName MsAcpi_ThermalZoneTemperature).CurrentTemperature"
    
    dados = {"atual": None, "alta": '80', "critica": '100'}

    try:
        process = subprocess.run(
            ["powershell", "-NoProfile", "-Command", cmd], 
            capture_output=True, 
            text=True, 
            check=True
        )
        
        output = process.stdout.strip()

        if output:
            temp_raw = float(output)
            dados["atual"] = round((temp_raw / 10.0) - 273.15, 2)
            
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}Erro de Permissão: Você precisa rodar o script como ADMINISTRADOR.{Style.RESET_ALL}")
    except ValueError:
        print(f"{Fore.YELLOW}Erro: O sistema retornou um valor inválido ou não suportado.{Style.RESET_ALL}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        
    return dados


def get_temp_linux() -> dict[str, float | None]:
    """
    Obtém a temperatura no Linux usando psutil.
    """
    # Inicializa o dicionário logo no início para evitar NameError
    dados = {"atual": None, "alta": None, "critica": None}

    try:
        temperaturas = psutil.sensors_temperatures()
    except AttributeError:
        # Caso o SO rodando não suporte a função sensors_temperatures
        return dados

    if "coretemp" in temperaturas and temperaturas["coretemp"]:
        # Busca pelo sensor principal (Package id 0)
        for s in temperaturas["coretemp"]:
            if s.label == "Package id 0":
                dados["atual"] = s.current
                dados["alta"] = s.high
                dados["critica"] = s.critical
                return dados  # Retorna assim que encontra

        # Backup: Se não achou o 'Package id 0', pega o primeiro sensor disponível
        s = temperaturas["coretemp"][0]
        dados["atual"] = s.current
        dados["alta"] = s.high
        dados["critica"] = s.critical

    return dados