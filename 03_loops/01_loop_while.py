#Bucle con una simple condicion

contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # Incrementa el contador en 1

#Bucle infinito con break

while True:
    entrada = input("Escribe 'salir' para terminar el bucle: ")
    if entrada.lower() == 'salir':
        print("Saliendo del bucle.")
        break  # Sale del bucle
    else:
        print("Has escrito:", entrada)

#Bucle con continue

numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue  # Salta el resto del codigo y vuelve al inicio del bucle
    print("Número impar:", numero)

#Bucle con else

contador = 0
while contador < 3:
    print("Contador en el bucle:", contador)
    contador += 1
else:
    print("El bucle ha terminado normalmente.")
#El bloque else se ejecuta cuando la condicion del while deja de cumplirse
#Si tengo un brak dentro del bucle, el else no se ejecuta ya que NUNCA se cumple la condicion de finalizacion normal


numero = -1
while numero < 0:
    try:
        numero = int(input("Introduce un número positivo: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
print("Has introducido el número positivo:", numero)