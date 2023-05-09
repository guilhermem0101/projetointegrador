import requests

url = 'https://www.workana.com/jobs?category=it-programming&language=pt&publication=1d'
params = {
    'category': 'it-programming',
    'language': 'pt',
    'publication': '1d'
}

response = requests.get(url, params=params)
data = response.json()

# Agora você pode trabalhar com os dados JSON retornados
