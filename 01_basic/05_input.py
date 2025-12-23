# Input de datos del usuario
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print(f"Hola {nombre}, tienes {edad} años.")

# El input siempre devuelve un string
print(f"El tipo de dato de edad es: {type(edad)}")

# Si queremos usar la edad como un numero, debemos castear
# Por ejemplo, para sumar 1 a la edad
edad_num = int(edad)
nueva_edad = edad_num + 1
print(f"El próximo año tendrás {nueva_edad} años.")

