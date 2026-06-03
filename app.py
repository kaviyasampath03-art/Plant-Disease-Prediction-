from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    value = float(request.form['value'])

    prediction = model.predict([[value]])

    return render_template(
        'index.html',
        prediction_text=f'Predicted Value: {prediction[0]:.2f}'
    )

if __name__ == '__main__':
    app.run(debug=True)

    