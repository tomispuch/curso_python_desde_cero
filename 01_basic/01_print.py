# Funciones en Python

#Print sirve para sacar un mensaje en la consola
print("Hola mundo")
print('Las comillas simples también funcionan, sirve para poner "Comillas e imprimir"')

# Podemos imprimir distintos valores
print("Python", 3.8, True)

#Podemos cambiar el separador, el default es espacio
print("Python", 3.8, True, sep="-")

#Podemos cambiar el final, el default es salto de línea
print("Hola mundo", end=" :) ")
print("Siguiente línea")

#Para ver los valores por defecto podemos seleccionar el nombre de la funcion

#Tambien hay distintos tipos de datos como ya se. int, float, str, bool, NoneType, list, tuple, dict, set
print(type(3))        # int
print(type(3.14))     # float
print(type("Hola"))   # str
print(type(True))     # bool
print(type(None))     # NoneType
print(type([1, 2, 3])) # list
print(type((1, 2, 3))) # tuple
print(type({"a": 1, "b": 2})) # dict
print(type({1, 2, 3})) # set
