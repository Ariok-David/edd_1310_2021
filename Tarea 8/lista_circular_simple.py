class Nodo:
    def __init__(self, value, siguiente = None):
        self.data = value
        self.siguiente = siguiente

class CircularList:
    def __init__(self):
        self.__ref = None

    def is_empty(self):
        return self.__ref == None

    def insert(self, value):
        if self.is_empty():
            self.__ref = Nodo(value)
            self.__ref.siguiente = self.__ref
        elif self.search(value):
            print("El numero ya existe en la lista intenta con otro")
        else:
            if value > self.__ref.data:
                curr_node = self.__ref
                while curr_node.siguiente != self.__ref:
                    curr_node = curr_node.siguiente
                self.__ref = Nodo(value, curr_node.siguiente.siguiente)
                curr_node.siguiente.siguiente = self.__ref
            else:
                curr_node = self.__ref
                while value > curr_node.siguiente.data:
                    curr_node = curr_node.siguiente
                curr_node.siguiente = Nodo(value, curr_node.siguiente)

    def transversal(self): #Por default y para ayuda imprimira primero self.__ref y ya despues los demas.
        curr_node = self.__ref
        if curr_node == self.__ref and curr_node != None:
            print(f"{curr_node.data} -->", end = "")
            curr_node = curr_node.siguiente
        while curr_node != self.__ref:
            print(f"{curr_node.data} -->", end = "")
            curr_node = curr_node.siguiente
        print(" ")

    def search(self, value):
        exist = False
        curr_node = self.__ref
        while curr_node.siguiente.data != self.__ref.data:
            if curr_node.siguiente.data == value:
                exist = True
            curr_node = curr_node.siguiente
        if curr_node.siguiente.data == self.__ref.data and curr_node.siguiente.data == value:
            exist = True
        return exist

    def remove(self, value):
        if self.__ref.siguiente == self.__ref:
            self.__ref = None
        elif value == self.__ref.data:
            curr_node = self.__ref
            while curr_node.siguiente != self.__ref:
                curr_node = curr_node.siguiente
            curr_node.siguiente = self.__ref.siguiente
            self.__ref = curr_node
        else:
            curr_node = self.__ref
            while curr_node.siguiente.data != value:
                curr_node = curr_node.siguiente
            curr_node.siguiente = curr_node.siguiente.siguiente
