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
    Obtém a temperatura no Windows via PowerShell (WMI).
    """
    cmd = "get-wmiobject msacpi_thermalzonetemperature -namespace root/wmi"
    dados = {"atual": None, "alta": None, "critica": None}

    try:
        process = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
        output = process.stdout

        if "CurrentTemperature" in output:
            for line in output.split('\n'):
                if "CurrentTemperature" in line:
                    temp_raw = int(line.split(':')[-1].strip())
                    # Converte de Kelvin (multiplicado por 10) para Celsius
                    dados["atual"] = (temp_raw / 10.0) - 273.15
                    return dados
        return dados
    except Exception:
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