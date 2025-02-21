from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'house_price_model.pkl')
if not os.path.exists(model_path):
    raise FileNotFoundError("Model file 'house_price_model.pkl' not found. Please train and save the model first.")

model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        prediction = model.predict([np.array(data)])

        # Convert prediction to thousands and float
        predicted_value = int(np.round(prediction[0] * 100, 2))

        print("Prediction:", predicted_value)  # Log the value in Flask terminal

        return jsonify({'prediction': predicted_value})
    except Exception as e:
        print("Error:", str(e))  # Log error in Flask terminal
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
  

