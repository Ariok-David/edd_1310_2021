class NodoDoble:
    def __init__(self, value, siguiente = None, anterior = None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head = None#NodoDoble(None, None, None)
        self.__tail = None#NodoDoble(None, None, None)
        self.__size = 0

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__head == None and self.__tail == None

    def append(self, value):
        nuevo = NodoDoble(value)
        if self.__head == None and self.__tail == None:
            self.__head = nuevo
            self.__tail = nuevo
        else:
            curr_node = self.__head
            while curr_node.next != None:
                curr_node = curr_node.next
            self.__tail = nuevo
            self.__tail.prev = curr_node
            curr_node.next = self.__tail
        self.__size = self.__size + 1

    def find_from_head(self, value):
        curr_node = self.__head
        cont = 0
        while curr_node.data != value:
            curr_node = curr_node.next
            cont = cont + 1
        return cont

    def find_from_tail(self, value):
        curr_node = self.__tail
        cont = 0
        while curr_node.data != value:
            curr_node = curr_node.prev
            cont = cont + 1
        return cont

    def remove_from_head(self, value):
        curr_node = self.__head
        if self.__head.data == value and self.__head.next != None:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__size = self.__size - 1
        else:
            sig = None
            ant = None
            while curr_node.data != value and curr_node.next != None:
                ant = curr_node
                curr_node = curr_node.next
                sig = curr_node.next
            if curr_node.data == value and sig != None:
                ant.next = sig
                sig.prev = ant
                self.__size = self.__size - 1
            elif curr_node.data == value and curr_node.prev != None and curr_node.next == None:
                ant.next = None
                self.__tail = ant
                self.__size = self.__size - 1
            elif curr_node.data == self.__head.data and curr_node.data == self.__tail.data and curr_node.data == value:
                self.__head = None
                self.__tail = None
                self.__size = self.__size - 1
            else:
                print("Este dato no se encuentra dentro de la lista")

    def remove_from_tail(self, value):
        curr_node = self.__tail
        if self.__tail.data == value and self.__tail.prev != None:
            self.__tail = self.__tail.prev
            self.__tail.next = None
            self.__size = self.__size - 1
        else:
            sig = None
            ant = None
            while curr_node.data != value and curr_node.prev != None:
                sig = curr_node
                curr_node = curr_node.prev
                ant = curr_node.prev
            if curr_node.data == value and ant != None:
                ant.next = sig
                sig.prev = ant
                self.__size = self.__size - 1
            elif curr_node.data == value and curr_node.next != None and curr_node.prev == None:
                sig.prev = None
                self.__head = sig
                self.__size = self.__size - 1
            elif curr_node.data == self.__tail.data and curr_node.data == self.__head.data and curr_node.data == value:
                self.__tail = None
                self.__head = None
                self.__size = self.__size - 1
            else:
                print("Este dato no se encuentra dentro de la lista")

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} -->", end = "")
            curr_node = curr_node.next
        print(" ")

    def reverse_transversal(self):
        curr_node = self.__tail
        while curr_node != None:
            print(f"{curr_node.data} -->", end = "")
            curr_node = curr_node.prev
        print(" ")
