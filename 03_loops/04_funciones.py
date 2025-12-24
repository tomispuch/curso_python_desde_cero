"""
Definicion de una funcion

def nombre_de_la_funcion(parametro1, parametro2):
    # Bloque de codigo de la funcion
    resultado = parametro1 + parametro2
    return resultado  # Devuelve el resultado de la funcion
"""

def saludar(nombre):
    saludo = f"Hola, {nombre}!"
    return print(saludo)

saludar("Juan")
saludar("María")

def sumar(a, b):
    return a + b

resultado_suma = sumar(5, 3)
print("Resultado de la suma:", resultado_suma)

# Documentar funciones

def restar(a, b):
    """Resta b de a y devuelve el resultado."""
    return a - b

#Parametros por defecto

def potencia(base, exponente=2):
    """Calcula la potencia de base elevado a exponente."""
    return base ** exponente

def describir_persona(nombre, edad, ciudad):
    descripcion = f"{nombre} tiene {edad} años y vive en {ciudad}."
    return descripcion

info_persona = describir_persona("Ana", 30, "Madrid")
print(info_persona)

#Arumentos por clave
describir_persona(ciudad="Barcelona", nombre="Luis", edad=25)
# Llamada con argumentos por clave permite cambiar el orden de los argumentos
#Es muy util ya que si en un futuro cambio el contrato de la funcion, esta no va a romepr el codigo que la llama

#Argumentos de longitud variable
def sumar_todos(*numeros):
    """Suma todos los numeros proporcionados como argumentos."""
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

#Argumentos de clave-valor variable (**kwargs)

def mostrar_info(**info):
    """Muestra la informacion proporcionada como argumentos clave-valor."""
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Carlos", edad=28, ciudad="Valencia")
# Podemos llamar a la funcion con cualquier numero de argumentos clave-valor
# Muy util para funciones que reciben muchas opciones de configuracion
mostrar_info(marca="Toyota", modelo="Corolla", año=2020, color="Rojo")
# Mezcla de tipos de argumentos
