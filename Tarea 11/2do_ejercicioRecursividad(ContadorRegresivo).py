def contador_regresivo_rec(num):
    if num > 0:
        print(num)
        contador_regresivo_rec(num - 1)

def main():
    contador_regresivo_rec(5)

main()
