persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero",
    "social": {
        "twitter": "@juan",
        "linkedin": "juan-linkedin"
    }
}
# Acceder a valores
print(persona["nombre"])          # Output: Juan
print(persona["social"]["twitter"])  # Output: @juan
# Modificar valores
persona["edad"] = 31
print(persona["edad"])            # Output: 31
# Agregar nuevos pares clave-valor
persona["hobby"] = "Fotografía"
print(persona["hobby"])           # Output: Fotografía
# Eliminar pares clave-valor
del persona["ciudad"]
print(persona)                    # Output: {'nombre': 'Juan', 'edad': 31, 'profesion': 'Ingeniero', 'social': {'twitter': '@juan', 'linkedin': 'juan-linkedin'}, 'hobby': 'Fotografía'}

persona.pop("profesion")
print(persona)                    # Output: {'nombre': 'Juan', 'edad': 31, 'social': {'twitter': '@juan', 'linkedin': 'juan-linkedin'}, 'hobby': 'Fotografía'}
# Devuelve el valor y lo elimina del diccionario

#Sobreescribir un diccionario con otro
otro_persona = {
    "nombre": "Ana",
    "edad": 28,
    "ciudad": "Barcelona"
}
persona.update(otro_persona)
print(persona)                    # Output: {'nombre': 'Ana', 'edad': 28, 'social': {'twitter': '@juan', 'linkedin': 'juan-linkedin'}, 'hobby': 'Fotografía', 'ciudad': 'Barcelona'}
# El diccionario persona ahora tiene los valores de otro_persona para las claves coincidentes


# Métodos útiles
claves = persona.keys()
print(claves)                     # Output: dict_keys(['nombre', 'edad', 'social', 'hobby', 'ciudad'])
valores = persona.values()
print(valores)                   # Output: dict_values(['Ana', 28, {'twitter': '@juan', 'linkedin': 'juan-linkedin'}, 'Fotografía', 'Barcelona'])
items = persona.items()
print(items)                     # Output: dict_items([('nombre', 'Ana'), ('edad', 28), ('social', {'twitter': '@juan', 'linkedin': 'juan-linkedin'}), ('hobby', 'Fotografía'), ('ciudad', 'Barcelona')])

# Iterar sobre un diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")