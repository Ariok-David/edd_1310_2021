from pila import Stack

'''
Se creara un metodo en donde se pondra como argumentos la pila donde se sacara el valor medio,
un contador que generara el caso base y una pila de ayuda que nos permitira guardar los valores
que no sean intermedios para despues poder volver a añadirlos a la pila princial.
'''
def pop_stack(pila, num, p_ayuda):
    if num > 0:
        a = pila.pop()
        p_ayuda.push(a)
        pop_stack(pila, num - 1, p_ayuda)
        pila.push(p_ayuda.pop())
    elif num == 0:
        pila.pop()
#Se creo otro metodo donde obtendremos el valor del contador para nuestro caso base e iniciara la recursividad.
def find_midle_value(pila):
    p = Stack()
    c = (pila.length() / 2)
    pop_stack(pila, int(c),p)


def main():
    pil = Stack()
    pil.push(8)
    pil.push(7)
    pil.push(6)
    pil.push(5)
    pil.push(4)
    pil.push(3)
    pil.push(2)

    find_midle_value(pil)

    pil.to_string()

main()
