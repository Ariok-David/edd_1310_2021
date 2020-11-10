from Clases.Juego import JuegoDeLaVida

prueba = JuegoDeLaVida(7, 7, 11, [[1, 2], [2, 1], [2, 2], [2, 3]])
print("Inicio")
prueba.imprime_grid()
prueba.evolucionar()

#Este Juego tiene dos versiones de funcionamiento de conteo de vecinos vivos.
##El primero es cuando el espacio definido es el unico que hay se pude caracterizar por que en las ezquinas solo cuenta los cuadros que estan dentro del grid.
##El segundo es para cuando este en un limite de grid este cuente como vecinos el inicio del otro limite algo parecido a lo de pacman donde si llegaba a un limite de pantalla aparecia de nuevo en el limite contrario.
##El modulo util.py es de uso exclusivo para la segunda version de conteo de vecinos vivos.
##El metodo de vecinos vivos se encuentra en la clase Juego.
