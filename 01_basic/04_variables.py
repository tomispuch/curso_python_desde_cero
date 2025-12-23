variable = "Valor"

print(variable)

# Podemos reasignar el valor de una variable
edad = 18
print(edad)

edad = 20
print(edad)

# Las variables pueden cambiar de tipo dinámicamente
#Tipado dinamico: El tipo de dato se determina en tiempo de ejecucion, no hay que declararlo 

nombre = "Tomas"
print(type(nombre))
nombre = 1234
print(type(nombre))

#Es de tipado fuerte, no hace conversion automatica entre tipos de datos. Ya lo vimos antes. 
nombre = "Tomas"
print(f"Hola {nombre}, tienes {edad} años.")

#f Strings: Cadenas de texto que permiten interpolacion de variables con {}, desde python 3.6 en adelante

#Forma NO recomendada de asignar variables
nombre, edad = "Tomas", 20 #En una linea se asignan varias variables

#Convencion: nombres en minusculas y con guion bajo para separar palabras
mi_variable = 10
mi_variable_con_nombre_muy_largo = 20

MI_CONSTANTE = 3.14  # Convencion para constantes, aunque Python no tiene constantes reales 

#Se puede especificar el tipo de dato de una variable (opcional)
altura: float = 1.75
es_estudiante: bool = True