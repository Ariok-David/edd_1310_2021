class NodoArbol:
    def __init__(self, value, left = None, right = None):
        self.data = value
        self.left = left
        self.right = right

def recorrido_pre(arbol, lista = list()):
    if arbol.left == None and arbol.right == None:
        lista.append(arbol.data)
    elif arbol.left == None and arbol.right != None:
        lista.append(arbol.data)
        recorrido_pre(arbol.right)
    elif arbol.right == None and arbol.left != None:
        lista.append(arbol.data)
        recorrido_pre(arbol.left)
    else:
        lista.append(arbol.data)
        recorrido_pre(arbol.left)
        recorrido_pre(arbol.right)
    print(lista)

arbol = NodoArbol("R", NodoArbol("V", NodoArbol("U"), NodoArbol("W", NodoArbol("X"), None)), NodoArbol("S", NodoArbol("P"), NodoArbol("Q")))

recorrido_pre(arbol)
