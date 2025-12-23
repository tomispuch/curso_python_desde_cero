lista = [1,2,3,4,5]

lista.append(6)  # Agrega el elemento 6 al final de la lista
print("Después de append:", lista)

lista.insert(2, 2.5)  # Inserta el elemento 2.5 en el índice 2
print("Después de insert:", lista)

lista.remove(4)  # Elimina el primer elemento con valor 4
print("Después de remove:", lista)

#Para ver mas ver la documentacion oficial de python

lista.pop()  # Elimina y devuelve el último elemento de la lista
print("Después de pop:", lista)

lista.pop(1)  # Elimina y devuelve el elemento en el índice 1
print("Después de pop(1):", lista)

del lista[1]  # Elimina el elemento en el índice 1
print("Después de del:", lista)

lista.clear()  # Elimina todos los elementos de la lista
print("Después de clear:", lista)

del lista[1:3]  # Elimina elementos desde el índice 1 hasta el 2
print("Después de del con slicing:", lista)

numeros = [3, 1, 4, 5, 2]
print("Antes de sort:", numeros)
numeros.sort()  # Ordena la lista en orden ascendente
print("Después de sort:", numeros)
#MODIFICA LA LISTA ORIGINAL, no crea una nueva lista

