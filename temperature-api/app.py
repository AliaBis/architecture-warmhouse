from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/temperature')
def get_temperature():
    location = request.args.get('location', 'unknown')
    #сгенерить ранд.значение темпы (будет меняться при каждолм вызове)
    temp = round(random.uniform(18.0, 30.0), 2)
    
    response = {
        "location": location,
        "temperature": temp,
        "unit": "Celsius"
    }
    print(f"запрос для {location}: {temp}°C")
    return jsonify(response)

if __name__ == '__main__':
    # Порт по умолчанию 8081
    app.run(host='0.0.0.0', port=8081)

    #http://localhost:8081/temperature?location=Bedroom
