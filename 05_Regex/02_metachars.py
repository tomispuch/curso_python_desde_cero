#Meta caracteres: Simbolos especiales con significado especial en las expresiones regulares
import re

#1. El punto (.): Representa cualquier caracter excepto el salto de linea
patron_punto = "H.la"
texto_punto = "Hola Hxla H1la H-la Hla"
resultados_punto = re.findall(patron_punto, texto_punto)
print("Resultados con punto:", resultados_punto)  # ['Hola', 'Hxla', 'H1la', 'H-la']   

#La forma correcta de referirse a una regex es con el prefijo r antes de las comillas
patron_punto_raw = r"H.la"

#Como busco los puntos?
patron_escapado = r"H\.la"  # El backslash (\) escapa el punto. Osea que cancela el significado especial del punto
texto_escapado = "H.la Hxla H1la H-la Hla"
resultados_escapado = re.findall(patron_escapado, texto_escapado)
print("Resultados con punto escapado:", resultados_escapado)  # ['H.la']

#2. El asterisco (*): Representa cero o mas repeticiones del caracter o grupo anterior
patron_asterisco = "Ho*la"  # La 'o' puede aparecer 0 o mas veces
texto_asterisco = "Hla Hola Hoola Hoooola"
resultados_asterisco = re.findall(patron_asterisco, texto_asterisco)

#3. \d: Representa cualquier digito (0-9)
texto = "Mi numero de telefono es 123-456-7890"
patron_digitos = r"\d\d\d-\d\d\d-\d\d\d\d"  # Busca el patron de numero de telefono
resultados_digitos = re.findall(patron_digitos, texto)
print("Digitos encontrados:", resultados_digitos)  # ['123-456-7890']

#Cuantificadores: Permiten especificar cuantas veces debe aparecer un caracter o grupo

texto = "Mi numero de telefono es 123-456-7890"
patron_cuantificadores = r"\d{3}-\d{3}-\d{4}"  # {n} indica exactamente n repeticiones
resultados_cuantificadores = re.findall(patron_cuantificadores, texto)
print("Digitos encontrados con cuantificadores:", resultados_cuantificadores)  # ['123-456-7890']

#4. \w: Representa cualquier caracter alfanumerico (letras, digitos, guion bajo)
texto_alfanumerico = "Usuario_123 tiene email 2@@dominio.com"
patron_alfanumerico = r"\w+"  # + indica una o mas repeticiones
resultados_alfanumerico = re.findall(patron_alfanumerico, texto_alfanumerico)
print("Caracteres alfanumericos encontrados:", resultados_alfanumerico)  # ['Usuario_123', 'tiene', 'email']

#5. \s: Representa cualquier espacio en blanco (espacios, tabulaciones, saltos de linea)
texto_espacios = "Hola,\neste es un\tejemplo."
patron_espacios = r"\s"  # Busca espacios en blanco
resultados_espacios = re.findall(patron_espacios, texto_espacios)
print("Espacios en blanco encontrados:", resultados_espacios)  # ['\n', ' ', '\t', ' ']

#6. ^ y $: Representan el inicio (^) y el final ($) de una cadena
texto_inicio_final = "Hola mundo"
patron_inicio = r"^Hola"  # Busca "Hola" al inicio
patron_final = r"mundo$"  # Busca "mundo" al final
resultado_inicio = re.search(patron_inicio, texto_inicio_final)
resultado_final = re.search(patron_final, texto_inicio_final)
print("Patron al inicio encontrado:", bool(resultado_inicio))  # True
print("Patron al final encontrado:", bool(resultado_final))    # True

#Verificar un numero
numero_telefono = "+54 11 1234-5678"
patron_telefono = r"^\+\d{2,3}\s\d{2}\s\d{4}-\d{4}$"
#Explicacion del patron:
# ^         : Inicio de la cadena
# \+        : Caracter literal '+'
# \d{2,3}   : Entre 2 y 3 digitos (codigo de pais)
# \s        : Espacio
# \d{2}     : 2 digitos (codigo de area)
# \s        : Espacio
# \d{4}-\d{4} : 4 digitos, un guion, y otros 4 digitos (numero local)
# $         : Final de la cadena

#EJERCICIO: Validar que un mail sea gmail
email = "tomasspuch@gmail.com"
patron_email = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
resultado_email = re.search(patron_email, email)
print("Email gmail valido:", bool(resultado_email))  # True
#Explicacion del patron:
# [a-zA-Z0-9._%+-]+ : Uno o mas caracteres permitidos en la parte local del email

#\b: Representa un limite de palabra
texto_limite_palabra = "Hola mundo, el mundovich es grande."
patron_limite_palabra = r"\bmundo\b"  # Busca la palabra "mundo" completa
resultados_limite_palabra = re.findall(patron_limite_palabra, texto_limite_palabra)
print("Palabras 'mundo' encontradas:", resultados_limite_palabra)  # ['mundo']

#7. | : Operador OR (o)
texto_or = "Me gusta el color rojo y el color azul."
patron_or = r"rojo|azul"  # Busca "rojo" o "azul"
resultados_or = re.findall(patron_or, texto_or)
print("Colores encontrados:", resultados_or)  # ['rojo', 'azul']