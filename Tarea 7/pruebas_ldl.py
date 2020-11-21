from lista_doblemente_ligada import DoubleLinkedList

l = DoubleLinkedList()

l.append(8)
l.append(2)
l.append(5)
l.append(2)
l.append(7)

l.transversal()
l.reverse_transversal()
print(f"Size: {l.get_size()}")
print(l.is_empty())

print(f"Hubicacion desde head de 8: {l.find_from_head(8)}")
print(f"Hubicacion desde tail de 8: {l.find_from_tail(8)}")

print(f"Hubicacion desde head de 2: {l.find_from_head(2)}") # Tomar en cuenta que existen dos nuemros dos asi que solo tomara en cuenta el primero que encuentre

print(f"Hubicacion desde head de 2: {l.find_from_tail(2)}") # Tomar en cuenta que existen dos nuemros dos asi que solo tomara en cuenta el primero que encuentre

print(f"Hubicacion desde head de 7: {l.find_from_head(7)}")
print(f"Hubicacion desde tail de 7: {l.find_from_tail(7)}")

print(f"Hubicacion desde head de 5: {l.find_from_head(5)}")
print(f"Hubicacion desde tail de 5: {l.find_from_tail(5)}")


l.remove_from_tail(8)
l.transversal()
l.reverse_transversal()
print(f"Size: {l.get_size()}")
print(l.is_empty())

l.remove_from_tail(7)
l.transversal()
l.reverse_transversal()
print(f"Size: {l.get_size()}")
print(l.is_empty())

l.remove_from_tail(5)
l.transversal()
l.reverse_transversal()
print(f"Size: {l.get_size()}")
print(l.is_empty())

l.remove_from_tail(2)
l.transversal()
l.reverse_transversal()
print(f"Size: {l.get_size()}")
print(l.is_empty())

l.remove_from_tail(2)
l.transversal()
l.reverse_transversal()
print(f"Size: {l.get_size()}")
print(l.is_empty())
