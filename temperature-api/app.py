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
    location = request.args.get('location', '').strip()
    sensor_id = request.args.get('sensorId', '').strip()
    if not location and not sensor_id:
        sensor_id = "1"
        location = location_mapping[sensor_id]
    elif sensor_id and not location:
        location = location_mapping.get(sensor_id)
        if not location:
            return jsonify({"error": "Invalid sensorId"}), 404
    elif location and not sensor_id:
        sensor_id = sensor_id_mapping.get(location)
        if not sensor_id:
            return jsonify({"error": "Location not found"}), 404
    elif location and sensor_id:
        if location_mapping.get(sensor_id) != location:
            return jsonify({"error": "Inconsistent sensorId and location"}), 400
    temperature = round(random.uniform(18.0, 26.0), 2)
    return jsonify({
        "location": location,
        "sensorId": sensor_id,
        "temperature": temperature,
        "unit": "Celsius"
    })

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
