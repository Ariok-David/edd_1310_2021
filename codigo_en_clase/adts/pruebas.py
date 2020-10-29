from arrays import Array
algo = Array(10)
print(algo.get_item(63))
print("-------------------------------")
algo.set_item(68, 0)
print(algo.get_item(0))
print("-------------------------------")
print(f"El arreglo tiene { algo.get_length() } elementos")
print("-------------------------------")
algo.clear( 3 )
print(algo.get_item(7))
print("-------------------------------")
for x in algo:
    print(x)
print("-------------------------------")
for x in range( algo.get_length() ):
    print(f"{x} -> { algo.get_item(x) }")
print("-------------------------------")
algo.set_item(15, 5)
algo.set_item(18, 1)
algo.set_item(4, 9)
for x in range( algo.get_length() ):
    print(f"{x} -> { algo.get_item(x) }")
print("-------------------------------")
