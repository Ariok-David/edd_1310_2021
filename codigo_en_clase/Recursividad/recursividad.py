#Creado hoy 12 de enero de 2021. Grupo: 1310
def factorial(n):
    resultado = 0
    if n== 0:
        return 1
    else:
        return factorial(n-1) * n

def printRev(n):
    if n > 0:
        print(n)
        printRev(n - 1)

def fibonacci(n):
    if n == 1 or n == 0:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

def main():
    for num in range(1,10,1):
        r = factorial(num)
        print(f"El factorial de {num} es {r}")
def main2():
    printRev(3)

def main3():
    for num in range(11):
        print(str(fibonacci(num)) + ",", end = "")

main3()
