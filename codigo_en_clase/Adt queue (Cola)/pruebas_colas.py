from colas import Queue
q1 = Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())


print("Prueba dos de Queue")
c1 =  {"id":1 , "Nombre":"Mario" , "Balance":20.5}
c2 =  {"id":2 , "Nombre":"Diana" , "Balance":3456.5}
c3 =  {"id":3 , "Nombre":"Bartolo" , "Balance":1000000.0}

atencion = Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente = atencion.dequeue()
print(f"Bienvenido Sr. {siguiente['Nombre']}, en que podemos servirle el dia de hoy")
