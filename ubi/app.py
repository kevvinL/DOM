from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_location', methods=['POST'])
def send_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    # Muestra las coordenadas en la terminal
    print(f"Ubicación recibida: Latitud={latitude}, Longitud={longitude}")

    return jsonify({"status": "success", "latitude": latitude, "longitude": longitude})

if __name__ == '__main__':
    app.run(debug=True)
