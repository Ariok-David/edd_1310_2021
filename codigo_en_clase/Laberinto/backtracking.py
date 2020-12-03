#Creado hoy 1 de diciembre de 2020
from Array2d import Array2D
from pila import Stack

class LaberintoADT:
    # 0 Pasillo
    # 1 Pared
    # S salida
    # E entrada
    #Pasillos es una tupla((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
    #Entrada en una tupla (5,1)
    #Salida en una tupla (2,5)
    def __init__(self, rens, cols, pasillos, entrada, salida):
        self.__laberinto = Array2D(rens, cols, '1')
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0],pasillo[1],'0')
        self.set_entrada(entrada[0],entrada[1]) #Añadido hoy 3 de diciembre de 2020
        self.set_salida(salida[0],salida[1]) # Añadido hoy 3 de diciembre de 2020
        self.__camino = Stack() #Anñadido hoy 3 de diciembre de 2020
        self.__previa = None #Añadido hoy 3 de diciembre de 2020

    def to_string(self):
        self.__laberinto.to_string()

#Creado hoy 3 de diciembre de 2020
    """
    Establece la entrada poniendo una 'E' en la matriz, verificar limites perifericos
    """
    def set_entrada(self, ren, col):
        try:
            self.__laberinto.set_item(ren, col, 'E')
        except Exception as e:
            print("Cordenadas fuera de rango del laberinto")

    """
    Establecer la salida dentro de los limites perifericos de la matriz
    """
    def set_salida(self, ren, col):
        try:
            self.__laberinto.set_item(ren, col, 'S')
        except Exception as e:
            print("Cordenadas fuera de rango del laberinto")

    def es_salida(self, ren, col):
        return self.__laberinto.get_item(ren, col) == 'S'

    def buscar_entrada(self):
        encontrado = False
        for renglon in range(self.__laberinto.get_num_rows()):
            for columna in range(self.__laberinto.get_num_cols()):
                if self.__laberinto.get_item(renglon,columna) == 'E':
                    self.__camino.push(tuple(renglon,columna))
                    encontrado = True
        return encontrado 

    def set_previa(self, pos_previa):
        self.__previa = pos_previa

    def get_previa(self):
        return self.__previa

    def resolver_laberinto(self):
        #Aplicar reglas
