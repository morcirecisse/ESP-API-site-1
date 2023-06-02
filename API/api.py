from flask import Flask, request, jsonify, render_template
import mysql.connector
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configuration de la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="iot_data"
)

# Création de la table pour stocker les données
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS sensor_data (id INT AUTO_INCREMENT PRIMARY KEY, temperature FLOAT, humidity FLOAT, pressure FLOAT)")

# Route pour recevoir les données de l'ESP
@app.route('/get', methods=['POST'])
def receive_sensor_data():
    data = request.get_json()
    temperature = data['temperature']
    humidity = data['humidity']
    pressure = data['pressure']

    # Enregistrement des données dans la base de données
    cursor.execute("INSERT INTO sensor_data (temperature, humidity, pressure) VALUES (%s, %s, %s)", (temperature, humidity, pressure))
    db.commit()

    return jsonify({'message': 'Données enregistrées avec succès'})


# Renvoi des données en temps réel
@app.route('/realtime', methods=['GET'])
def realtime():
    cnx = pymysql.connect(user='root', password='', host='localhost', database='iot_data')
    cursor = cnx.cursor()
    cursor.execute("SELECT temperature, humidity, pressure FROM sensor_data ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()
    cnx.close()
    print(result)
    return {"temperature": result[0], "humidity": result[1], "pressure": result[2]}

# Site web
@app.route('/lecture')
def display_data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM sensor_data")
    data = cursor.fetchall()

    return render_template('index.html', data=data) 

# Route pour afficher les données de température dans le tableau HTML
@app.route('/temperature', methods=['GET'])
def temperature():
    cnx = pymysql.connect(user='root', password='', host='localhost', database='iot_data')
    cursor = cnx.cursor()
    cursor.execute("SELECT temperature FROM sensor_data ORDER BY id DESC")
    result = cursor.fetchall()
    cursor.close()
    cnx.close()

    # Formater les données sous forme d'un tableau d'objets JSON
    temperature_data = [{'temperature': temperature} for (temperature,) in result]
    
    return jsonify(temperature_data)

# Route pour afficher les données d'humidité dans le tableau HTML
@app.route('/humidity', methods=['GET'])
def humidity():
    cnx = pymysql.connect(user='root', password='', host='localhost', database='iot_data')
    cursor = cnx.cursor()
    cursor.execute("SELECT humidity FROM sensor_data ORDER BY id DESC")
    result = cursor.fetchall()
    cursor.close()
    cnx.close()

    # Formater les données sous forme d'un tableau d'objets JSON
    humidity_data = [{'humidity': humidity} for (humidity,) in result]
    
    return jsonify(humidity_data)

# Route pour afficher les données de pression dans le tableau HTML
@app.route('/pressure', methods=['GET'])
def pressure():
    cnx = pymysql.connect(user='root', password='', host='localhost', database='iot_data')
    cursor = cnx.cursor()
    cursor.execute("SELECT pressure FROM sensor_data ORDER BY id DESC")
    result = cursor.fetchall()
    cursor.close()
    cnx.close()

      # Formater les données sous forme d'un tableau d'objets JSON
    pressure_data = [{'pressure': pressure} for (pressure,) in result]
    
    return jsonify(pressure_data)

# Lancement de l'API
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

