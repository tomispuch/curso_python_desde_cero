"""
Aprender Regex en Python

- Sirven para buscar patrones en cadenas de texto.
- Validacion de datos
- Manipulacion de texto: Extraer, reemplazar y modificar texto.

"""
#1. Importar el modulo de expresiones regulares 
import re #Si o si para manejar expresiones regulares en Python

#2. Crear un patron de busqueda
patron = "Hola"

#3. El texto donde lo quremos buscar
texto = "Hola, este es un ejemplo de expresiones regulares. Hola de nuevo!"

#4. Usar la funcion de busqueda "re"
resultado = re.search(patron, texto)

if resultado:
    print("Patron encontrado!")
    print("Posicion:", resultado.start(), "-", resultado.end())
else:
    print("Patron no encontrado.")

#IMPORTANTE: Resultado es un objeto Match, NO una cadena
resultado.group()  # Devuelve el texto que coincide con el patron
print("Texto encontrado:", resultado.group())
print("Posicion inicio:", resultado.start())
print("Posicion fin:", resultado.end())


#EJERCICIO
#Encuentra la primera ocurrencia de la palabra "IA" en el sieguiente texto e indica en que posicion empieza y termina.
texto_ejercicio = "La inteligencia artificial (IA) es una rama de la informática que se centra en la creación de sistemas capaces de realizar tareas que normalmente requieren inteligencia humana. La IA está transformando diversas industrias, desde la atención médica hasta la automoción."

patron_ejercicio = "IA"
resultado = re.search(patron_ejercicio, texto_ejercicio)
if resultado:
    print("Patron encontrado!")
    print("Posicion inicio:", resultado.start())
    print("Posicion fin:", resultado.end())

#Encontrar todas las coincidencias de la palabra "IA" en el texto
resultados = re.findall(patron_ejercicio, texto_ejercicio)
print("Todas las coincidencias de 'IA':", resultados)
#Ahora no tiene sentido ya que el patron es lo mismo de lo que queremos buscar

#Iterar sobre todas las coincidencias y mostrar sus posiciones
matches = re.finditer(patron_ejercicio, texto_ejercicio) #Devuelve un iterable de objetos Match
for match in matches:
    print("Coincidencia encontrada en posicion:", match.start(), "-", match.end())

#Modificadores: Opciones quese pueden agregar a un patron para cambiar su comportamiento
#Ejemplo: Hacer la busqueda sin importar mayusculas o minusculas
patron_modificador = "ia"
resultado_modificador = re.search(patron_modificador, texto_ejercicio, re.IGNORECASE) #El tercer parametro es el modificador
if resultado_modificador:
    print("Patron encontrado con modificador!")
    print("Posicion inicio:", resultado_modificador.start())
    print("Posicion fin:", resultado_modificador.end())

#Reemplazar todas las ocurrencias de "IA" por "Inteligencia Artificial"
texto_modificado = re.sub(patron_ejercicio, "Inteligencia Artificial", texto_ejercicio)
print("Texto modificado:", texto_modificado)

