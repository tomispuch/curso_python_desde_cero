#Castear es cambiar el valor de un tipo de dato a otro

print("Castear un entero a float:", float(5))      # De int a float
print("Castear un float a int:", int(3.99))        # De float a int (pierde la parte decimal, OJO con esto)

#print("100" + 2) # Esto da error porque no se puede sumar str con int, PYTHON no castea automaticamente
print("Castear un str a int:", int("100") + 2)     # De str a int

print(bool(3))
print(bool(0)) ##El unico que se convierte a false es el 0, lo mismo con la cadena de texto vacia ""
print(bool(-1))