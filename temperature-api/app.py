

    #http://localhost:8081/temperature?location=Bedroom


import random
from flask import Flask, request, jsonify

app = Flask(__name__)

location_mapping = {
    "1": "Living Room",
    "2": "Bedroom",
    "3": "Kitchen",
    "4": "Bathroom",
    "5": "Hallway" 
}
sensor_id_mapping = {v: k for k, v in location_mapping.items()}

@app.route('/temperature', methods=['GET'])
def get_temperature():
    """
    Возвращает случайное значение температуры для указанного location.
    Если location не указан, используется значение по умолчанию.
    Если location не найден, возвращается ошибка.
    """
    location = request.args.get('location', '').strip()
    sensor_id = request.args.get('sensorId', '').strip()
    if not location and sensor_id:
        location = location_mapping.get(sensor_id)
        if not location:
            return jsonify({"error": "Invalid sensorId provided"}), 400
    elif location and not sensor_id:
        if location not in sensor_id_mapping:
            return jsonify({"error": f"Location '{location}' not found"}), 400
        sensor_id = sensor_id_mapping[location]
    elif not location and not sensor_id:
        default_sensor_id = list(location_mapping.keys())[0]
        location = location_mapping[default_sensor_id]
        sensor_id = default_sensor_id
        print(f"No location or sensorId provided, using default: {location} (sensorId: {sensor_id})")
    elif location and sensor_id:
        if sensor_id not in location_mapping or location_mapping[sensor_id] != location:
            return jsonify({"error": "Provided location and sensorId are inconsistent"}), 400
    if not location:
        return jsonify({"error": "Could not determine location"}), 400
    #генерится рандомное значение темпы(например, от -10 до +30 градусов Цельсия)
    temperature = round(random.uniform(-10.0, 30.0), 2)
    return jsonify({
        "location": location,
        "sensorId": sensor_id,
        "temperature": temperature
    })

if __name__ == '__main__':

#http://127.0.0.1:5000/temperature?location=Living Room
#http://127.0.0.1:5000/temperature?sensorId=2
#http://127.0.0.1:5000/temperature
# http://127.0.0.1:5000/temperature?location=Bathroom
# http://127.0.0.1:5000/temperature?sensorId=5

    app.run(debug=True)
