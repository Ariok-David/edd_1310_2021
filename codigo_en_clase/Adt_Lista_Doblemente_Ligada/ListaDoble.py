# Creado hoy 24-Noviembre-2020 grupo 1310

class NodoDoble:
    def __init__(self, valor, anterior = None, siguiente = None):
        self.data = valor
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head = NodoDoble(None)
        self.__tail = NodoDoble(None)
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def append(self, value):
        if self.is_empty():
            nuevo = NodoDoble(value)
            self.__head = nuevo
            self.__tail = nuevo

        else:
            nuevo = NodoDoble(value, self.__tail, None)
            self.__tail.next = nuevo
            self.__tail = nuevo
        self.__size += 1

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} --> ", end = "")
            curr_node = curr_node.next
        print(" ")

    def reverse_transversal(self):
        curr_node = self.__tail
        while curr_node != None:
            print(f"{curr_node.data} --> ", end = "")
            curr_node = curr_node.prev
        print(" ")

    def remove_from_head(self, value):
        curr_node = self.__head
        if self.__head.data == value:#si head es igual a value
            self.__head = self.__head.next
            self.__head.prev = None
            self.__tail = self.__tail.
        while curr_node.data != value and curr_node != None:
            curr_node = curr_node.next
        if curr_node.data == value:
            curr_node.prev.next = curr_node.next
            curr_node.next.prev = curr_node.prev
        curr_node.next = None
        curr_node.prev = None
        self.__size -= 1
