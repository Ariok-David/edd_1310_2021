#Creado hoy 19 de Enero de 2021. Grupo : 1310
#Modificado y terminada hoy 21 de Enero de 2021. Grupo : 1310
class NodoArbol:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert(self, value):
        #Regla 1
        if self.__root == None: #Self.__root is None
            self.__root = NodoArbol(value, None, None)
        #Regla 2
        else:
            self.__insert__(self.__root, value)

    def __insert__(self, nodo, value):
        if nodo.data == value:
            print("El dato ya existe, no se añadira nada")
        elif value < nodo.data:
            #Regla 1
            if nodo.left == None:
                nodo.left = NodoArbol(value)
            #Regla 2
            else:
                self.__insert__(nodo.left, value)
        else:
            if nodo.right == None:
                nodo.right = NodoArbol(value)
            else:
                self.__insert__(nodo.right, value)

    def __recorrido_in(self, nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data, end = " , ")
            self.__recorrido_in(nodo.right)

    def __recorrido_pos(self, nodo):
        if nodo:
            self.__recorrido_pos(nodo.left)
            self.__recorrido_pos(nodo.right)
            print(nodo.data, end = " , ")

    def __recorrido_pre(self, nodo):
        if nodo:
            print(nodo.data, end = " , ")
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)

    def transversal(self, format = "inorden"):
        if format == "inorden":
            self.__recorrido_in(self.__root)
        elif format == "preorden":
            self.__recorrido_pre(self.__root)
        elif format == "posorden":
            self.__recorrido_pos(self.__root)
        else:
            print("Error, ese recorrido no existe")
        print("")

    def search(self, value):
        if self.__root == None:
            return None
        else:
            return self.__search(self.__root, value)

    def __search(self, nodo, value):
        if nodo == None:
            print("Caso base")
            return None
        elif nodo.data == value:
            print("Encontrado")
            return nodo
        elif value < nodo.data:
            print("Buscar a la izquierda")
            return self.__search(nodo.left, value)
        else:
            print("Buscar a la derecha")
            return self.__search(nodo.right, value)

    def remove(self, value):
        encontrado = self.search(value)
        #caso 1
        if encontrado.left == None and encontrado.right == None:
            print("Eliminando", encontrado.data)
            encontrado = None
        #caso 2
        elif (encontrado.left != None and encontrado.right == None) or (encontrado.left == None and encontrado.right != None):
            print("A eliminar", encontrado.data)
