#Creado hoy 1 de diciembre de 2020
from backtracking import LaberintoADT
pasillos_inicial = ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lab = LaberintoADT(6,6,pasillos_inicial, (5,2), (2,5)) # Modificado hoy 3 de diciembre de 2020
lab.to_string()
