import numpy as np
import pickle

from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

with open('logistic_model.pkl', 'rb') as f:
    model = pickle.load(f)

print('Model loaded. Start serving...')
print('Check http://127.0.0.1:5000/')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/wellness', methods=['GET'])
def wellness():
    return render_template('wellness_advice.html')

@app.route('/medicines', methods=['GET'])
def medicines():
    return render_template('medicines.html')

@app.route('/contact_us', methods=['GET'])
def contact_us():
    return render_template('contact_us.html')

@app.route('/', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            age = int(request.form['age'])
            gender = int(request.form['gender'])
            polyuria = int(request.form['Polyuria'])
            polydipsia = int(request.form['Polydipsia'])
            weight = int(request.form['Weight'])
            weakness = int(request.form['Weakness'])
            polyphagia = int(request.form['Polyphagia'])
            thrush = int(request.form['Thrush'])
            blurring = int(request.form['Blurring'])
            itching = int(request.form['Itching'])
            irritability = int(request.form['Irritability'])
            healing = int(request.form['Healing'])
            paresis = int(request.form['Paresis'])
            stiffness = int(request.form['Stiffness'])
            alopecia = int(request.form['Alopecia'])
            obesity = int(request.form['Obesity'])

            new_pat = [[age, gender, polyuria, polydipsia, weight, weakness, polyphagia, thrush, blurring, itching, irritability, healing, paresis, stiffness, alopecia, obesity]]

            result = model.predict(new_pat)
            val = "Diabetes" if result[0] == 1 else "No Diabetes"
            return render_template('index.html', value=val)
    except Exception as e:
        print(f"An error occurred: {e}")
        val = "Error in prediction. Please check the input values."
    return render_template('index.html', value=val)

if __name__ == '__main__':
    app.run(debug=True)