from colas_con_prioridad_acotada import BoundedPriorityQueue
#Se crea la cola del barco.
cpa = BoundedPriorityQueue(7)

#Se comprobara que el barco esta vacio para empezar a ingresar los pasajros.
print(f"El barco esta vacio: {cpa.is_empty()}")
print("Los tripulantes pueden ingresar.")

#Tripulantes
Maestres = {"prioridad": 4, "descripcion":"Maestre", "Personas":["Juan P", "Diego H"]}
Niños = {"prioridad": 2, "descripcion":"Niños", "Personas":["Santi H", "Angel H"]}
Mecanicos = {"prioridad": 4, "descripcion":"Mecanicos", "Personas":["Diana T", "Maria H"]}
Mujeres = {"prioridad": 3, "descripcion":"Mujeres", "Personas":["Tamara A", "Alexandra L"]}
TerceraEdad = {"prioridad": 2, "descripcion":"3ra Edad", "Personas":["Valentina F", "Gabriela L", "Daniel D"]}
Niñas = {"prioridad": 1, "descripcion":"Niñas", "Personas":["Cristina M", "America R"]}
Hombres = {"prioridad": 3, "descripcion":"Hombres", "Personas":["Pedro B", "Arturo G"]}
Vigia = {"prioridad": 4, "descripcion":"Vigia", "Personas":["Itzel J"]}
Capitan = {"prioridad": 5, "descripcion":"Capitan", "Personas":["Wendi T"]}
Timonel = {"prioridad": 4, "descripcion":"Timonel", "Personas":["Alejandro L", "Luis M"]}

#Los tripulantes comensaran a tripular el barco.
cpa.enqueue(Maestres['prioridad'], Maestres)
cpa.enqueue(Niños['prioridad'], Niños)
cpa.enqueue(Mecanicos['prioridad'], Mecanicos)
cpa.enqueue(Mujeres['prioridad'], Mujeres)
cpa.enqueue(TerceraEdad['prioridad'], TerceraEdad)
cpa.enqueue(Niñas['prioridad'], Niñas)
cpa.enqueue(Hombres['prioridad'], Hombres)
cpa.enqueue(Vigia['prioridad'], Vigia)
cpa.enqueue(Capitan['prioridad'], Capitan)
cpa.enqueue(Timonel['prioridad'], Timonel)

#El barco esta lleno?
print(f"El barco esta lleno: {not cpa.is_empty()}")

#Recuento de pasajeros y su prioridad.
print("------------------Recuento de pasajeros y su prioridades-------------------")
cpa.to_string()

#Los tripulandes abandonan el Barco.
print("------------------Evacuacion del Barco-----------------------")
while  (not cpa.is_empty()):
    print(f"Han abandonado el barco: {cpa.dequeue()}")
if cpa.is_empty():
    print("El barco ha sido evacuado por completo")
