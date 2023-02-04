import webbrowser
import requests
from bs4 import BeautifulSoup

# Abrir la página de búsqueda de Google
webbrowser.open('https://www.google.com/search?q=python')

# Realizar una solicitud a la página de búsqueda de Google
response = requests.get('https://www.google.com/search', params={'q': 'python'})

# Procesar el contenido de la respuesta con BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Imprimir el título de cada resultado de la búsqueda
for result in soup.find_all('h3'):
  print(result.text)