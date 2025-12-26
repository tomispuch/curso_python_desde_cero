import re

#Cuantificadores: Permiten especificar cuantas veces debe aparecer un caracter o grupo

#1. *: Cero o mas repeticiones
patron_asterisco = r"Ho*la"  # La 'o' puede aparecer 0 o mas veces
texto_asterisco = "Hla Hola Hoola Hoooola"
resultados_asterisco = re.findall(patron_asterisco, texto_asterisco)
print("Resultados con asterisco:", resultados_asterisco)  # ['Hla', 'Hola', 'Hoola', 'Hoooola']

#2. +: Una o mas repeticiones
patron_mas = r"Ho+la"  # La 'o' debe aparecer al menos una vez
texto_mas = "Hla Hola Hoola Hoooola"
resultados_mas = re.findall(patron_mas, texto_mas)
print("Resultados con mas:", resultados_mas)  # ['Hola', 'Hoola',   'Hoooola']

#3. ?: Cero o una repeticion
patron_interrogacion = r"Ho?la"  # La 'o' puede aparecer 0 o 1 vez
texto_interrogacion = "Hla Hola Hoola"
resultados_interrogacion = re.findall(patron_interrogacion, texto_interrogacion)
print("Resultados con interrogacion:", resultados_interrogacion)  # ['Hla', 'Hola']