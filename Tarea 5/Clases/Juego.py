from Clases.Array2D import Array_2D
from Clases.util import *

class  JuegoDeLaVida:
    CELULA_VIVA = 1
    CELULA_MUERTA = 0

    def __init__(self, ren, col, generaciones, poblacion):
        self.__largo = col
        self.__alto = ren
        self.__grid = Array_2D(self.__largo, self.__alto)
        self.__generaciones = generaciones
        for celula in poblacion:
            self.__grid.set_item(celula[0],celula[1],self.CELULA_VIVA)

    def imprime_grid(self):
        for r in range(self.__grid.get_row_size()):
            for c in range(self.__grid.get_col_size()):
                if self.__grid.get_item(r, c) == 1:
                    print("▓▓", end = "")
                else:
                    print("░░", end = "")
            print("")

    def get_num_rows(self):
        return self.__grid.get_row_size()

    def get_num_cols(self):
        return self.__grid.get_col_size()

    def set_celula_muerta(self, row, col):
        self.__grid.set_item(row, col, self.CELULA_MUERTA)

    def set_celula_viva(self, row, col):
        self.__grid.set_item(row, col, self.CELULA_VIVA)

    def get_is_viva(self, row, col):
        return self.__grid.get_item(row, col) == self.CELULA_VIVA

    def get_is_muerta(self, row, col):
        return self.__grid.get_item(row, col) == self.CELULA_MUERTA

    def get_numero_vecinos_vivos(self, row, col):
        vecinos_vivos = 0
        for r in range(row-1, row+2):
            for c in range(col-1, col+2):
                try:
                    if self.__grid.get_item(r, c) == self.CELULA_VIVA:
                        vecinos_vivos += self.CELULA_VIVA
                except Exception as e:
                    vecinos_vivos += self.CELULA_MUERTA
                #if self.__grid.get_item(check_rows(r,self.__grid.get_row_size()), check_cols(c, self.__grid.get_col_size())) == self.CELULA_VIVA:
                    #vecinos_vivos += self.CELULA_VIVA
        if self.__grid.get_item(row, col) == self.CELULA_VIVA:
            vecinos_vivos = vecinos_vivos - 1
        return vecinos_vivos

    def evolucionar(self):
        for gen in range(self.__generaciones):
            ayuda = Array_2D(self.__largo, self.__alto)
            for r in range(self.__grid.get_row_size()):
                for c in range(self.__grid.get_col_size()):
                    if self.get_is_viva(r, c):
                        if 2 <= self.get_numero_vecinos_vivos(r, c) <= 3:
                            ayuda.set_item(r, c, self.CELULA_VIVA)
                        if 0 <= self.get_numero_vecinos_vivos(r, c) <= 1:
                            ayuda.set_item(r, c, self.CELULA_MUERTA)
                        if 4 <= self.get_numero_vecinos_vivos(r, c) <= 9:
                            ayuda.set_item(r, c, self.CELULA_MUERTA)
                    if self.get_is_muerta(r, c):
                        if self.get_numero_vecinos_vivos(r, c) == 3:
                            ayuda.set_item(r, c, self.CELULA_VIVA)
            self.__grid = ayuda
            print(f"Generacion {gen + 1}")
            self.imprime_grid()
