#Creado hoy 07 de Enero de 2021. Grupo: 1310
from colas_con_prioridad_acotada import BoundedPriorityQueue

maestres = {"prioridad": 4, "descripcion":"Maestre", "Personas":["Juan P", "Diego H"]}
ninos = {"prioridad": 2, "descripcion":"Niños", "Personas":["Santi H", "Angel H"]}
mecanicos = {"prioridad": 4, "descripcion":"Mecanicos", "Personas":["Diana T", "Maria H"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'], maestres)
cpa.enqueue(ninos['prioridad'], ninos)
cpa.enqueue(mecanicos['prioridad'], mecanicos)
cpa.to_string()
