class Nodo:
    def __init__(self, value, siguiente = None):
        self.data = value  #Falta encapsulamiento
        self.siguiente = siguiente

class LinkedList:
    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head == None

    def append(self, value):
        nuevo = Nodo( value )
        if self.__head == None:
            self.__head = nuevo # self.is_empty()
        else:
            curr_node = self.__head
            while curr_node.siguiente != None:
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} -->", end = "")
            curr_node = curr_node.siguiente
        print(" ")

    def remove(self, value):
        curr_node = self.__head
        if self.__head.data == value:
            self.__head = self.__head.siguiente
        else:
            anterior = None
            while curr_node.data != value and curr_node.siguiente != None:
                anterior = curr_node
                curr_node = curr_node.siguiente
            if curr_node.data == value:
                #print("ACTUAL:", anterior.data)
                anterior.siguiente = curr_node.siguiente
            else:
                    print("El dato no existe en la lista")

    def preppend(self, value):
        nuevo = Nodo(value, self.__head)
        self.__head = nuevo

    def tail(self):
        curr_node = self.__head
        while curr_node.siguiente != None:
            curr_node = curr_node.siguiente
        return curr_node

    def get(self, posicion = None): #Por defecto regresa el ultimo
        contador  = 0
        dato = None
        if posicion == None:
            dato = self.tail().data
        else:
            #TAREA 6 --------------------------------------------------------------------------
            curr_node = self.__head
            while contador != posicion and curr_node.siguiente != None:
                curr_node = curr_node.siguiente
                contador = contador + 1
            if contador == posicion: # Buscaremos por que se detubo el while.
                dato = curr_node.data
            else:
                dato = "Rango fuera de la lista"
            #TAREA 6 --------------------------------------------------------------------------
        return dato
