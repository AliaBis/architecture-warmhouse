# architecture-warmhouse/temperature_api/app.py
import random
from flask import Flask, request, jsonify
from datetime import datetime # Импортируем datetime

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
    # Получаем оба параметра, которые могут быть переданы
    location = request.args.get('location', '').strip()
    sensor_id_str = request.args.get('sensorId', '').strip() # Используем sensor_id_str, чтобы не путать с int

    # Логика определения location и sensor_id
    if sensor_id_str:
        # Если передан sensorId, определяем location
        temp_location = location_mapping.get(sensor_id_str)
        if not temp_location:
            return jsonify({"error": "Invalid sensorId"}), 404
        if location and temp_location != location:
            return jsonify({"error": "Inconsistent sensorId and location"}), 400
        location = temp_location
    elif location:
        # Если передан location, определяем sensorId
        temp_sensor_id = sensor_id_mapping.get(location)
        if not temp_sensor_id:
            return jsonify({"error": "Location not found"}), 404
        sensor_id_str = temp_sensor_id
    else:
        # По умолчанию берем Living Room (sensor_id 1)
        sensor_id_str = "1"
        location = location_mapping[sensor_id_str]

    temperature_value = round(random.uniform(18.0, 26.0), 2)
    status = "active" if temperature_value > 20 else "inactive"
    current_time = datetime.now().isoformat(timespec='milliseconds') + "Z" # Формат ISO 8601 с миллисекундами и Z

    return jsonify({
        "location": location,
        "sensor_id": sensor_id_str, # Меняем 'sensorId' на 'sensor_id'
        "value": temperature_value,  # Меняем 'temperature' на 'value'
        "unit": "Celsius",
        "timestamp": current_time,
        "status": status,
        "sensor_type": "temperature",
        "description": f"Current temperature in {location}"
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
