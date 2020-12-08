#Creado hoy 1 de diciembre de 2020
from backtracking import LaberintoADT
import time
pasillos_inicial = ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lab = LaberintoADT(6,6,pasillos_inicial, (5,2), (2,5))
lab.buscar_entrada() # Modificado hoy 3 de diciembre de 2020
#Creado hoy 8 de diciembre de 2020
lab.to_string()
#Imprimir Laberinto
lab.imprimir_camino()

while (not lab.es_salida(lab.get_pos_actual()[0], lab.get_pos_actual()[1])):
    lab.resolver_laberinto()
    lab.imprimir_camino()
    time.sleep(1.0)
