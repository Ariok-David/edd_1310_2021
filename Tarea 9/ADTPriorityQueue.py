class PriorityQueue:
    def __init__(self):
        self.__data = list()

    def is_empty(self):
        return len(self.__data) == 0

    def lenght(self):
        return len(self.__data)

    def enqueue(self, prioridad, elemento):
        #se buscara la posicion en donde se añadira el objeto con (priorida y elemento)
        posicion = 0
        for objet in self.__data:
            if prioridad >= objet[0]:
                posicion += 1
        #Se aplicaran algunas condiciones para añadir el objeto en la posicion que le corresponde.
        if self.is_empty() or self.lenght() == posicion:
            self.__data.append((prioridad, elemento))
        else:
            self.__data.insert(posicion, (prioridad, elemento))

    def dequeue(self):
        return self.__data.pop(0)

    def to_string(self):
        cadena = ""
        for objet in self.__data:
            cadena = cadena + " | " + str(objet)
        cadena = cadena + "|"
        return cadena
