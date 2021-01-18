print("-----------Arbol 1 -----------------")
prefijo1 = ["+", "-", 5, 4, "*", 3, 2]
posfijo1 = [5, 4, "-", 3, 2, "*", "+"]
infijo1 = [5, "-", 4, "+", 3, "*", 2]
print("\nPrefijo:")
for valor in prefijo1:
    print(f"{str(valor)}  ==>  ", end = "")
print("\nPosfijo:")
for valor in posfijo1:
    print(f"{str(valor)}  ==>  ", end = "")
print("\nInfijo:")
for valor in infijo1:
    print(f"{str(valor)}  ==>  ", end = "")

print("\n\n-----------Arbol 2 -----------------")
prefijo2 = [40, 30, 25, 35, 50, 45, 60]
posfijo2 = [25, 35, 30, 45, 60, 50, 40]
infijo2 = [25, 30, 35, 40, 45, 50, 60]
print("\nPrefijo:")
for valor in prefijo2:
    print(f"{str(valor)}  ==>  ", end = "")
print("\nPosfijo:")
for valor in posfijo2:
    print(f"{str(valor)}  ==>  ", end = "")
print("\nInfijo:")
for valor in infijo2:
    print(f"{str(valor)}  ==>  ", end = "")
