from Clases.Trabajadores import Trabajador
from Clases.Arrays import Array
import datetime as dt

#Metodo para solo mostrar el archivo en su forma original.
def mostrar_archivo(nombre_archivo):
    archivo = open(nombre_archivo, 'rt')
    datos = archivo.read()
    print(datos)
    archivo.close()

#Metodo para ordenar y guardar los trabajadores en un array.
def obtener_objetos_trabajador(nombre_archivo):
    archivo = open(nombre_archivo, 'rt')
    trabajadores = archivo.readlines() #se leeran todas la lineas del archivo para mejor comodidad.
    clases_trabajador = Array(len(trabajadores) - 1)# se crea el array que contendra a los trabajadores.
    for count in range(1, len(trabajadores)): # se leeran linea por linea los trabajadores del archivo.
        trabajador = trabajadores[count].strip('\n ').split(',')# se eliminaran saltos de linea
        empleado = Trabajador(trabajador[0], trabajador[1], trabajador[2], trabajador[3], trabajador[4], trabajador[5], trabajador[6])# se crea el objeto trabajador y se guarda en empleado
        clases_trabajador.set_item(empleado, count - 1)# se guarda el objeto empleado en el Array.
    archivo.close()
    return clases_trabajador

#metodo para sacar el menor o mayor numero de antiguedad de todos los Trabajadores.
def antiguedad(ar, mnmy):
    mayor = ar.get_item(0).antiguedad_trabajador()
    menor = ar.get_item(0).antiguedad_trabajador()
    for trab in ar:
        ant = trab.antiguedad_trabajador()
        if ant > mayor:
            mayor = ant
        if ant < menor:
            menor = ant
        if mnmy == '+':
            a = mayor
        if mnmy == '-':
            a = menor
    return a

# Metodo que imprimira el o los trabajadores con mas antiguedad.
def mostrar_trabajadores_con_mayor_antiguedad(arr):
    for trab in arr:
        if trab.antiguedad_trabajador() == antiguedad(arr, '+'):
            print(f"{trab.get_nombres()} {trab.get_paterno()} con {trab.antiguedad_trabajador()} años de Antiguedad.")

# Metodo que imprimira el o los trabajadores con menor antiguedad.
def mostrar_trabajadores_con_menor_antiguedad(arr):
    for trab in arr:
        if trab.antiguedad_trabajador() == antiguedad(arr, '-'):
            print(f"{trab.get_nombres()} {trab.get_paterno()} con {trab.antiguedad_trabajador()} años de Antiguedad.")
