from src.monitor.software.processos import capturar_processos

import time

while True:
    lista_processos = capturar_processos(3)

    if lista_processos:
        for p in lista_processos:
            if p['uso_cpu'] > 0:
                print(f"Processo: {p['nome']} | PID: {p['pid']} | Usuário: {p['usuario']} | Uso CPU: {p['uso_cpu']} | Memória: {p['memoria']}")
    time.sleep(5)