class Array_2D:
    def __init__(self, rows, cols):
        self.__cols = cols
        self.__rows = rows
        self.__array = [[0 for x in range(self.__cols)] for y in range(self.__rows)]

    def get_row_size(self):
        return len(self.__array)

    def get_col_size(self):
        return len(self.__array[0])

    def set_item(self, ren, col, dato):
        try:
            self.__array[ren][col] = dato
        except Exception as e:
            print("Posicion fuera de rango.")

    def get_item(self, ren, col):
        try:
            dato = self.__array[ren][col]
        except Exception as e:
            return "Error"#Posicion fuera de rango.")
        return dato

    def clear(self, dato):
        for ren in range(self.__rows):
            for col in range(self.__cols):
                self.__array[ren][col] = dato

    def to_string(self):
        return self.__array
