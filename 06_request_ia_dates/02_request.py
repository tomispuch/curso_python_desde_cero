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


#2, Con dependencias externas (usando requests)
import requests

response = requests.get(api_posts) # Hacer una petición GET a la URL (PARECIDO A SpringBoot)

if response.status_code == 200: # Verificar que la respuesta sea exitosa (código 200)
    json_data = response.json() # Obtener los datos en formato JSON directamente
    print(json_data)
else:
    print("Error en la petición:", response.status_code)

# Requests maneja automáticamente la apertura y cierre de la conexión
# También maneja errores de red y HTTP de manera más sencilla
# Además, es más fácil de usar y leer el código
# Por estas razones, requests es la opción preferida para hacer peticiones HTTP en Python  

#Hacer un post
post_data = {
    "title": "Prueba de POST",
    "body": "Este es el contenido de la prueba de POST",
    "userId": 1
}
response = requests.post(api_posts, json=post_data) # Hacer una petición POST


if response.status_code == 201: # Verificar que la respuesta sea exitosa (código 201 para creación)
    json_data = response.json()
    print("POST creado:", json_data)
else:
    print("Error en la petición POST:", response.status_code)


#Hacer un put
api_posts_put = "https://jsonplaceholder.typicode.com/posts/1" # URL para actualizar el post con ID 1


put_data = {
    "id": 1,
    "title": "Prueba de PUT",
    "body": "Este es el contenido de la prueba de PUT",
    "userId": 1
}
response = requests.put(api_posts_put, json=put_data) # Hacer una petición PUT
if response.status_code == 200: # Verificar que la respuesta sea exitosa (código 200)
    json_data = response.json()
    print("POST actualizado:", json_data)
else:
    print("Error en la petición PUT:", response.status_code)


#Usar la API de OpenAI