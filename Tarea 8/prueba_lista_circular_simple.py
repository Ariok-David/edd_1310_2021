from lista_circular_simple import CircularList
cl = CircularList()
#Prueba de is_empty()
print(f"La lista esta vacia: {cl.is_empty()}")

#Prueba de is_empty() dos y de insert()
print("-------------------------------------")
cl.insert(1)
print(f"La lista esta vacia: {cl.is_empty()}")

#Prueba de transversal()
cl.insert(2)
cl.insert(3)
cl.insert(4)
cl.insert(6)
cl.insert(8)
print("-------------------------------------")
cl.transversal()

#Prueba de intento de insertar numeros ya existentes en la lista
print("-------------------------------------")
cl.insert(1)
cl.insert(2)
cl.insert(3)
cl.insert(4)
cl.insert(6)
cl.insert(8)
cl.transversal()

#Prueba de insercion de dato mayor esperamos que se vuelva ref
print("-------------------------------------")
cl.insert(9)
cl.transversal()

#Prueba de insercion en medio
print("-------------------------------------")
cl.insert(5)
cl.insert(7)
cl.transversal()

#Prueba de insercion de dato menor que todos los que ya estan en la lista
print("-------------------------------------")
cl.insert(0)
cl.transversal()

#Prueba de search en la lista; si todo sale bien todos saldran true
print("-------------------------------------")
print(cl.search(0))
print(cl.search(1))
print(cl.search(2))
print(cl.search(3))
print(cl.search(4))
print(cl.search(5))
print(cl.search(6))
print(cl.search(7))
print(cl.search(8))
print(cl.search(9))
print(cl.search(11))

#Prueba de remove en los __ref
print("-------------------------------------")
cl.remove(9)
cl.transversal()
cl.remove(8)
cl.transversal()

#prueba de remove en datos intermedios
print("-------------------------------------")
cl.remove(2)
cl.transversal()
cl.remove(4)
cl.transversal()

#Prueba de remove en el dato siguiente de __ref
print("-------------------------------------")
cl.remove(0)
cl.transversal()
cl.remove(6)
cl.transversal()

#Prueba de vaciado de lista con remove
print("-------------------------------------")
cl.remove(1)
cl.transversal()
cl.remove(3)
cl.transversal()
cl.remove(5)
cl.transversal()
cl.remove(7)
cl.transversal()
print(f"La lista esta vacia: {cl.is_empty()}")
