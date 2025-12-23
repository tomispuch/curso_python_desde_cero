lista1 = [1,2,3,4,5]
lista2 = ["a","b","c","d","e"]
lista3 = [1,"b",3.5,True] #Lista de tipos mixtos

#Acceso por indice
print(lista1[0])  # Imprime el primer elemento de lista1
print(lista2[2])  # Imprime el tercer elemento de lista2
print(lista3[-1])  # Imprime el ultimo elemento de lista3 cuenta al revez

#Slicing (rebanado)
print(lista1[1:4])  # Imprime elementos desde el indice 1 hasta el 3
print(lista2[:3])   # Imprime los primeros tres elementos
print(lista3[2:])  # Imprime desde el indice 2 hasta el final

print(lista1[0:5:2])  # Imprime elementos desde el indice 0 hasta el 4 con un paso de 2
print(lista2[::-1])  # Imprime la lista al reves

#Modificar elementos
lista1[0] = 10
print(lista1)  # Imprime [10, 2, 3, 4, 5]

#Agregar elementos
lista1.append(6)
print(lista1)  # Imprime [10, 2, 3, 4, 5, 6]
lista2.insert(1, "x")
print(lista2)  # Imprime ['a', 'x', 'b', 'c', 'd', 'e']
lista1 += [7, 8, 9]
print(lista1)  # Imprime [10, 2, 3, 4, 5, 6, 7, 8, 9]

#Eliminar elementos
lista1.remove(3)
print(lista1)  # Imprime [10, 2, 4, 5, 6, 7, 8, 9]
del lista2[0]
print(lista2)  # Imprime ['x', 'b', 'c', 'd', 'e']