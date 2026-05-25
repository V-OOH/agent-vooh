from detectar import identificar
from src.database.database import buscar_id_display

busca = buscar_id_display("a4:63:a1:6e:67:09")
print(busca)

i = identificar("Linux")
print(i)
