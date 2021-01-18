class NodoArbol:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

def recorrido_pos(arbol, lista = list()):
    if arbol.left == None and arbol.right == None:
        recorrido_pre(arbol.left)
        recorrido_pre(arbol.right)
        lista.append(arbol.data)
    #    else:
        #lista.append(arbol.data)
    print(lista)

arbol = NodoArbol("R", NodoArbol("V", NodoArbol("U"), NodoArbol("W", NodoArbol("X"), NodoArbol("Y"))), NodoArbol("S", NodoArbol("P"), NodoArbol("Q")))

recorrido_pos(arbol)
