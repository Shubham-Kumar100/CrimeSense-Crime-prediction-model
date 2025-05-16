from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open('crime_prediction_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(request.form[x]) for x in ['Year', 'Month', 'Day', 'DayOfWeek', 'Minute', 'Second', 'Latitude', 'Longitude']]
    prediction = model.predict([features])[0]
    return render_template('index.html', prediction_text=f'Predicted Crime Type: {prediction}')

if __name__ == '__main__':
    app.run(debug=True)


