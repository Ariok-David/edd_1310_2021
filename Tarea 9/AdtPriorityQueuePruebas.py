from ADTPriorityQueue import PriorityQueue

#Creamos la cola con prioridad
q1 = PriorityQueue()
#Comprobamos si esta vacia (True).
print(f"La cola esta vacia: {q1.is_empty()}")
#Añadimos los tripulantes en la cola con prioridad.
q1.enqueue(4, "Maestre")
q1.enqueue(2, "Niños")
q1.enqueue(4, "Mecanico")
q1.enqueue(3, "Hombres")
q1.enqueue(4, "Vigia")
q1.enqueue(5, "Capitan")
q1.enqueue(4, "Timonel")
q1.enqueue(3, "Mujeres")
q1.enqueue(2, "3ra Edad")
q1.enqueue(1, "Niñas")
#Comprobamos si esta vacia de nuevo(False).
print(f"La cola esta vacia: {q1.is_empty()}")
#Comprobamos cuantos elementos tiene la cola(10).
print(f"Elementos en la cola: {q1.lenght()}")
#Comprobamos la cola
print(q1.to_string())
#Comprobamos el dequeue para checar si salen en el orden correcto.
a = 0
while not q1.is_empty():
    a += 1
    print(f"{a}° en salir son {q1.dequeue()}")
    print(f"Elementos en la cola: {q1.lenght()}")

print(f"La cola esta vacia: {q1.is_empty()}")
