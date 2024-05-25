import requests as rq
URL =  'https://httpbin.org/get'

# Realizar peticion get
response = rq.get(URL)
print(response)

# Acceder aL estado de la peticion 
print(response.status_code)

# Acceder al cuerpo de la URL (str)
print(response.text)

# A formato json
print(response.json()) # dict

# Acceso a algunas keys del json o dict
print(response.json()['url'])
print(response.json())

# Obtener url de la petición
print(response.url)