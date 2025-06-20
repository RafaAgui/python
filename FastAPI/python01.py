import requests
print("Hello, World!")


apiUrl = "https://apiejemplos.azurewebsites.net/api/Empleados/19"

response = requests.get(apiUrl)
jsonObject = response.json()
print(jsonObject)
print("fin de programa")