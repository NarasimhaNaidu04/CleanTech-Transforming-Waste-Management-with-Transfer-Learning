from flask import Flask, render_template, request, jsonify
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes (important for frontend access)

model = load_model('vgg16_model.h5')
classes = ['Biodegradable', 'Recyclable', 'Trash']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save uploaded file
    filepath = os.path.join('static', file.filename)
    file.save(filepath)

    # Preprocess image
    img = image.load_img(filepath, target_size=(224, 224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.0

    # Predict
    prediction = model.predict(img_tensor)
    predicted_class = classes[np.argmax(prediction)]

    return jsonify({
        'prediction': predicted_class,
        'image_path': '/' + filepath
    })

if __name__ == '__main__':
    app.run(debug=True, port=2222)

