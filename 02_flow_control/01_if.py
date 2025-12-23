import os
os.system("clear")  # Limpia la consola (funciona en Unix/Linux y Windows)

#Ahi estamos importando la biblioteca del sistema operativo para usar un comando del sistema operativo

edad = 18

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#Cuidado con la sintaxis, es todo con tabulado.    
#El bloque de codigo que va a ejecutar el condicional es el que esta tabulado despues de los dos puntos ":"

nota = 7

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 5:
    print("Aprobado")
else:
    print("Suspenso")

#Una vez que una condicion se cumple, no se evaluan las siguientes. Revisa de arriba a abajo.


edad = 20
tiene_carnet = True

if edad >= 18 and tiene_carnet:
    print("Puedes conducir.")
 
# not = !
if not tiene_carnet:
    print("No tienes carnet de conducir.")

#Se interpreta como True cualquier valor diferente de cero o una cadena no vacia
numero = 3
if numero:
    print("El numero es diferente de cero.")

#La condicion ternaria

# codigo si se cumple if condicion else codigo si no se cumple
edad = 16
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje)

#Se escribe asi ya que es la forma mas parecida al lenguaje natural.