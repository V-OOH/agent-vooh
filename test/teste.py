import time
from time import sleep

# import psutil
# from psutil import cpu_percent
#
# while True:
#     processos = psutil.Process(31821)
#     nucleos = psutil.cpu_count(logical=True)
#
#     p = processos
#     while True:
#         print(p.cpu_percent(interval=5) / nucleos)
# # print(list(psutil.Process().as_dict().keys()))

from src.monitor.software.processos import capturar_processos

p = capturar_processos(2)
print(p)