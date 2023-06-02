import random
import requests
import time

# Fonction pour générer des données aléatoires
def generate_random_data():
    temperature = random.uniform(10, 30)  
    humidity = random.uniform(40, 70)  
    pressure = random.uniform(900, 1100)  
    return temperature, humidity, pressure

# Fonction pour envoyer les données à l'API
def send_data_to_api(data):
    url = 'http://localhost:5000/get'  
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        print("Données envoyées avec succès à l'API")
    else:
        print("Échec de l'envoi des données à l'API")

# Boucle principale pour simuler l'envoi de données de l'ESP
while True:
    temperature, humidity, pressure = generate_random_data()
    data = {
        'temperature': temperature,
        'humidity': humidity,
        'pressure': pressure
    }
    send_data_to_api(data)
    time.sleep(5)  
