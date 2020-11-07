class Array2D:

    def __init__(self,rows, cols, value):
        self.__cols = cols
        self.__rows = rows
        self.__array=[[value for x in range(self.__cols)] for y in range(self.__rows)]

    def to_string(self):
        [print("---",end="") for x in range(self.__cols)]
        print("")
        for ren in self.__array:
            print(ren)
        [print("---",end="") for x in range(self.__cols)]
        print("")

    def get_num_rows(self):
        return self.__rows

    def get_num_cols(self):
        return self.__cols

    def get_item(self,row,col):
        return self.__array[row][col]

    def set_item( self , row , col , valor ):
        self.__array[row][col]=valor

    def clearing(self, valor=0):
        for ren in range(self.__rows):
            for col in range(self.__cols):
                self.__array[ren][col]=valor



















from arrays import Array2D

class Juego:
    CELULA_VIVA = 1
    CELULA_MUERTA = 0

    def __init__(self,rens,cols,generaciones,poblacion):
        self.largo = cols
        self.alto = rens
        self.grid = Array2D( self.alto , self.largo,0 )
        self.generaciones = generaciones

        for celula in poblacion:
            self.grid.set_item(celula[0],celula[1],self.CELULA_VIVA)




def configura_generacion(self,nueva_poblacion):
        self.grid.clearing()
        for celula in nueva_poblacion:
            self.grid.set_item(celula[0],celula[1],self.CELULA_VIVA)


    def imprime_grid(self):
        for r in range(self.grid.get_num_rows()):
            for c in range(self.grid.get_num_cols()):
                if self.grid.get_item(r,c) == 0:
                    print("░░",end="")
                else:
                    print("▓▓",end="")
            print("")



            return self.alto



 def get_num_rows(self):
        return self.alto

    def get_num_cols(self):
        return self.largo

    def set_celula_muerta(self, row, col):
        self.grid.set_item(row, col, self.CELULA_MUERTA)

    def set_celula_viva( self , row , col):
        self.grid.set_item(row, col, self.CELULA_VIVA)

    def get_is_viva( self , row , col ):
        return self.grid.get_item(row,col) == self.CELULA_VIVA



    def get_num_cols(self):
        return self.largo

    def set_celula_muerta(self, row, col):
        self.grid.set_item(row, col, self.CELULA_MUERTA)

    def set_celula_viva( self , row , col):
        self.grid.set_item(row, col, self.CELULA_VIVA)

    def get_is_viva( self , row , col ):
        return self.grid.get_item(row,col) == self.CELULA_VIVA



















print("░░",end="")
print("▓▓",end="")
