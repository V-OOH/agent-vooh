from src.database.database import conectar
from src.database.database import buscar_id_display
from colorama import Fore, Style, init
import sys

#
# conexao = conectar()
#
# id_display = buscar_id_display("a4:63:a1:6e:67:09")

# No início do seu script principal:
display = buscar_id_display("a4:63:a1:6e:67:09")

if display:
    print(display['id'])
    print(display['mac'])

