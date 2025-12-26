#Como hacer peticiones a APIs con Python
#Con y sin dependiencas

#1. Sin dependencias externas (usando urllib)
import urllib.request
# Biblioteca de python que permite abrir una URL como si fuera un archivo
import json
# Biblioteca para manejar datos en formato JSON

api_posts = "https://jsonplaceholder.typicode.com/posts"

response = urllib.request.urlopen(api_posts) #Esto esta diciendo a python que abra la URL
# La variable response ahora contiene la respuesta del servidor

data = response.read() #Leer el contenido de la respuesta
# La variable data ahora contiene los datos en formato bruto (bytes)

json_data = json.loads(data.decode('utf-8'))
print(json_data) #Imprimir los datos en formato JSON

response.close() #Cerrar la conexión. IMPORTANTE

#Todo esto es Asincrono, es decir, el programa espera a que se complete la petición antes de continuar

#Lo ideal es hacerlo con try cath

try:
    response = urllib.request.urlopen(api_posts)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
except Exception as e:
    print("Ocurrió un error al hacer la petición:", e)