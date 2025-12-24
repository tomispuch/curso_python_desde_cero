nums = range(5) # Crea un rango de 0 a 4, no una lista
print("Rango de 0 a 4:", list(nums))  # Convierte el rango en una lista para mostrarlo

# O podemos usar un for
for num in range(5):
    print("Número en rango de 0 a 4:", num)

# Rango con inicio y fin Y PASO

nums_paso = range(2, 10, 2)  # Crea un rango de 2 a 9 con paso de 2
print("Rango de 2 a 9 con paso de 2:", list(nums_paso))

# Rango inverso
nums_inverso = range(10, 0, -1)  # Crea un rango de 10 a 1
print("Rango de 10 a 1:", list(nums_inverso))

#Repetir una accion
for _ in range(3):  # El guion bajo es una convención para variables que no se usan
    print("¡Hola, mundo!")