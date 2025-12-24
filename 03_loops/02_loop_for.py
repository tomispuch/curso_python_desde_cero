numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print("Número:", numero)

# Iterar sobre una cadena
palabra = "Python"
for letra in palabra:
    print("Letra:", letra)

# enumerate para obtener el indice y el valor
for indice, valor in enumerate(numeros):
    print(f"Índice: {indice}, Valor: {valor}")


# break

for numero in numeros:
    if numero == 3:
        print("Se encontró el número 3, saliendo del bucle.")
        break
    print("Número:", numero)

#Comprehension de listas

cuadrados = [numero**2 for numero in numeros]
print("Cuadrados:", cuadrados)

