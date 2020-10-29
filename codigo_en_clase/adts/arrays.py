class Array:
    #Generacion del Array
    def __init__( self , tam ):
        self.__info = [ 0 for x in range(tam)]

    #Obtencion del tado en la posicion deseada
    def get_item( self , posicion ):
        dato = 0
        try:
            dato = self.__info[ posicion ]
        except Exception as e:
            #print("Error de posicion")
            dato = "Error: Busca un dato fuera del rango del Array"
        return dato

    #Guardar un dato en la posicion deseada
    def set_item( self , dato , posicion ):
        try:
            self.__info[ posicion ] = dato
        except Exception as e:
            print("Error de posicion")

    #Obtener tamaño del Array
    def get_length( self ):
        return len ( self.__info )

    #Vaciar todos los datos del array tengan el valor dato.
    def clear( self , dato ):
        self.__info = [ dato for x in range( len( self.__info ) )]

    #Iterador del array
    def __iter__( self ):
        return _IteradorArreglo( self.__info )

#Creacion de un iterador para poder pasar todos los datos del Array
class _IteradorArreglo:
    def __init__( self , arr):
        self.__arr = arr
        self.__indice = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self.__indice < len( self.__arr ):
            dato = self.__arr[ self.__indice ]
            self.__indice += 1
            return dato
        else:
            raise StopIteration
