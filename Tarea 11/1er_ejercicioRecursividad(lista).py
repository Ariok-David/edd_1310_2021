def suma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop() + suma_lista_rec(lista)

def main():
    lis = [6, 4, 5, 3, 2]
    suma = suma_lista_rec(lis)
    print(suma)

main()
