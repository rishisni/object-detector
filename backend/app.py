from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import cv2
import os
from flask_cors import CORS
import numpy as np  
import datetime
import base64
app = Flask(__name__)
CORS(app)  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'

db = SQLAlchemy(app)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), unique=True, nullable=False)
    data = db.Column(db.LargeBinary, nullable=False)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'webp','avif'}

# def detect_objects(image_data):
#     nparr = np.frombuffer(image_data, np.uint8)
#     image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
#     car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     cars = car_cascade.detectMultiScale(gray, 1.1, 3)
#     for (x, y, w, h) in cars:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
#     car_count = len(cars)
#     return image, car_count

def detect_objects(image_data):
    nparr = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Load cascade classifiers for cars, trucks, and bikes
    car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')
    truck_cascade = cv2.CascadeClassifier('haarcascade_truck.xml')  # Assuming you have a 'haarcascade_truck.xml' file
    bike_cascade = cv2.CascadeClassifier('haarcascade_bike.xml')    # Assuming you have a 'haarcascade_bike.xml' file

    if image is None:
        raise ValueError("Error: Unable to read the image.")

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect cars
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)
    car_count = len(cars)

    # Detect trucks
    trucks = truck_cascade.detectMultiScale(gray, 1.1, 1)
    truck_count = len(trucks)

    # Detect bikes
    bikes = bike_cascade.detectMultiScale(gray, 1.1, 1)
    bike_count = len(bikes)

    # Draw bounding boxes around detected objects (optional)
    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    for (x, y, w, h) in trucks:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    for (x, y, w, h) in bikes:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Return processed image and counts
    return image, car_count, truck_count, bike_count

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        
        current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{current_datetime}_{secure_filename(file.filename)}"
        image_data = file.read()

        try:
            processed_image, car_count, truck_count, bike_count = detect_objects(image_data)

            _, processed_image_encoded = cv2.imencode('.jpg', processed_image)
            processed_image_base64 = base64.b64encode(processed_image_encoded).decode('utf-8')

            return jsonify({
                'message': 'Image uploaded successfully',
                'car_count': car_count,
                'truck_count': truck_count,
                'bike_count': bike_count,
                'processed_image': processed_image_base64
            })
        except ValueError as e:
            return jsonify({'error': str(e)})

    return jsonify({'error': 'File not allowed'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
