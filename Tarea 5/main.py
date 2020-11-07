from Clases.Juego import JuegoDeLaVida

prueba = JuegoDeLaVida(7, 7, 11, [[1, 2], [2, 1], [2, 2], [2, 3]])
print("Inicio")
prueba.imprime_grid()
prueba.evolucionar()
