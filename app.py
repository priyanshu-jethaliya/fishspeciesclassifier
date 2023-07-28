from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__, static_folder='static')

# Load the trained model
model = joblib.load('fish_species_classifier_model.joblib')
le = joblib.load('label_encoder.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    length = data['length']
    width = data['width']
    height = data['height']
    weight = data['weight']

    try:
        # Make prediction using the loaded model
        prediction = model.predict([[length, width, height, weight]])
        species = le.inverse_transform(prediction)[0]
        return jsonify({'species': species})

    except Exception as e:
        print("Prediction error:", e)  # Add this line for debugging
        return jsonify({'species': 'Prediction Error'})

    # Make prediction using the loaded model
    prediction = model.predict([[length, width, height, weight]])
    species = le.inverse_transform(prediction)[0]

    return jsonify({'species': species})

if __name__ == '__main__':
    # Use the PORT environment variable if available, otherwise use 5000 (local development)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
