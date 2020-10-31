from Utilidades import *

#Se mostrara el contenido del archivo junio.dat como referencia.
print("\n<-------------------------------------junio.dat------------------------------------------->\n")
mostrar_archivo('junio.dat')

#Obtenemos el Array de objetos Trabajador.
trabajadores = obtener_objetos_trabajador('junio.dat')

#Aplicamos formato a los datos obtenidos del archivo junio.dat.
print("\n<-------------------------------junio.dat con formato------------------------------------->\n")
for trabajador in trabajadores:
    print(trabajador.to_string()) # con el metodo to_string le daremos formato para que sean entendibles los datos del archivo.

#Mostramos el sueldo de cada trabajador.
print("\n<-------------------------------Sueldos por trabajador------------------------------------>\n")
for trabajador in trabajadores:
    tbr = trabajador.obtener_sueldo_de_trabajador()
    print(f"El trabajador: {tbr.get_item(0)} tiene un sueldo de {tbr.get_item(1) + tbr.get_item(2)} con prestaciones de {tbr.get_item(3)}")

#Mostramos el o los trabajadores mas antiguos.
print("\n<----------------------------Trabajador/es con mas antiguedad----------------------------->\n")
mostrar_trabajadores_con_mayor_antiguedad(trabajadores)

#Mostramos el o los trabajadores con menor antiguedad.
print("\n<---------------------------Trabajador/es con menos antiguedad---------------------------->\n")
mostrar_trabajadores_con_menor_antiguedad(trabajadores)
