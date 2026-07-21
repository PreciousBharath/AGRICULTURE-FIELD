import pickle
from flask import Flask, render_template, request, redirect, url_for, session, flash
import numpy as np

# ─────────────────────────────────────────────
app = Flask(__name__)
app.secret_key = 'agripredict-secret-2026-change-in-production'

# ─── Simple in-memory user store (replace with a real DB for production) ───
users_db = {}  # { email: { 'first_name', 'last_name', 'password', 'state' } }

# ─── Load ML model ───
model = pickle.load(open('model.pkl', 'rb'))

# ─── Fertilizer suggestions ───
fertilizer_suggestions = {
    0: "Arecanut: Apply 500g NPK 10:10:20 per plant annually.",
    1: "Other Kharif pulses: Apply 25kg Urea + 50kg DAP per acre.",
    2: "Rice: Apply 100kg N + 50kg P2O5 + 50kg K2O per hectare.",
    3: "Banana: Apply 200g N, 100g P2O5, 150g K2O per plant monthly.",
    4: "Cashewnut: Apply 400g NPK 10:10:20 per tree annually.",
    5: "Coconut: Apply 1kg NPK 10:10:20 per tree every 6 months.",
    6: "Dry ginger: Apply 50kg FYM + 25kg NPK 12:12:17 per acre.",
    7: "Sugarcane: Apply 120kg N + 60kg P2O5 + 60kg K2O per hectare.",
    8: "Sweet potato: Apply 30kg N + 20kg P2O5 per acre.",
    9: "Tapioca: Apply 60kg N + 40kg P2O5 + 40kg K2O per hectare.",
    10: "Black pepper: Apply 500g NPK 10:10:20 per vine annually.",
    11: "Dry chillies: Apply 50kg NPK 12:12:17 per hectare.",
    12: "Other oilseeds: Apply 25kg N + 50kg P2O5 per hectare.",
    13: "Turmeric: Apply 50kg NPK 12:12:17 per hectare.",
    14: "Maize: Apply 120kg N + 60kg P2O5 + 60kg K2O per hectare.",
    15: "Moong (Green Gram): Apply 20kg N + 40kg P2O5 per hectare.",
    16: "Urad: Apply 20kg N + 40kg P2O5 per hectare.",
    17: "Arhar/Tur: Apply 25kg N + 50kg P2O5 per hectare.",
    18: "Groundnut: Apply 50kg N + 50kg P2O5 + 50kg K2O per hectare.",
    19: "Sunflower: Apply 60kg N + 40kg P2O5 + 20kg K2O per hectare.",
    20: "Bajra: Apply 40kg N + 20kg P2O5 per hectare.",
    21: "Castor seed: Apply 50kg N + 50kg P2O5 per hectare.",
    22: "Cotton (lint): Apply 120kg N + 60kg P2O5 + 60kg K2O per hectare.",
    23: "Horse-gram: Apply 20kg N + 30kg P2O5 per hectare.",
    24: "Jowar: Apply 40kg N + 20kg P2O5 per hectare.",
    25: "Korra: Apply 40kg N + 20kg P2O5 per hectare.",
    26: "Ragi: Apply 30kg N + 20kg P2O5 per hectare.",
    27: "Tobacco: Apply 100kg N + 50kg P2O5 + 50kg K2O per hectare.",
    28: "Gram: Apply 20kg N + 40kg P2O5 per hectare.",
    29: "Wheat: Apply 120kg N + 60kg P2O5 + 40kg K2O per hectare.",
    30: "Masoor: Apply 20kg N + 40kg P2O5 per hectare.",
    31: "Sesamum: Apply 25kg N + 25kg P2O5 per hectare.",
    32: "Linseed: Apply 25kg N + 25kg P2O5 per hectare.",
    33: "Safflower: Apply 30kg N + 30kg P2O5 per hectare.",
    34: "Onion: Apply 50kg N + 50kg P2O5 + 50kg K2O per hectare.",
    35: "Other misc. pulses: Apply 20kg N + 40kg P2O5 per hectare.",
    36: "Samai: Apply 30kg N + 20kg P2O5 per hectare.",
    37: "Small millets: Apply 25kg N + 20kg P2O5 per hectare.",
    38: "Coriander: Apply 25kg N + 25kg P2O5 per hectare.",
    39: "Potato: Apply 100kg N + 50kg P2O5 + 100kg K2O per hectare.",
    40: "Other Rabi pulses: Apply 20kg N + 40kg P2O5 per hectare.",
    41: "Soyabean: Apply 50kg N + 50kg P2O5 per hectare.",
    42: "Beans & Mutter (Vegetable): Apply 25kg N + 25kg P2O5 per hectare.",
    43: "Bhindi: Apply 50kg N + 50kg P2O5 + 50kg K2O per hectare.",
    44: "Brinjal: Apply 50kg N + 50kg P2O5 + 50kg K2O per hectare.",
    45: "Citrus Fruit: Apply 200g NPK 10:10:20 per tree monthly.",
    46: "Cucumber: Apply 50kg N + 50kg P2O5 + 50kg K2O per hectare.",
    47: "Grapes: Apply 500g NPK 10:10:20 per vine annually.",
    48: "Mango: Apply 500g NPK 10:10:20 per tree annually.",
    49: "Orange: Apply 500g NPK 10:10:20 per tree annually.",
    50: "Other fibres: Apply 25kg N + 25kg P2O5 per hectare.",
    51: "Other Fresh Fruits: Apply 200g NPK 10:10:20 per plant annually.",
    52: "Other Vegetables: Apply 50kg N + 50kg P2O5 + 50kg K2O per hectare.",
    53: "Papaya: Apply 200g NPK 10:10:20 per plant monthly.",
    54: "Pome Fruit: Apply 500g NPK 10:10:20 per tree annually.",
    55: "Tomato: Apply 5kg FYM + 100g NPK 12:12:17 per 100 m².",
    56: "Mesta: Apply 25kg N + 25kg P2O5 per hectare.",
    57: "Cowpea (Lobia): Apply 25kg N + 25kg P2O5 per hectare.",
    58: "Lemon: Apply 500g NPK 10:10:20 per tree monthly.",
    59: "Pome Granet: Apply 500g NPK 10:10:20 per tree annually.",
    60: "Sapota: Apply 500g NPK 10:10:20 per tree annually.",
    61: "Cabbage: Apply 50kg N + 50kg P2O5 + 50kg K2O per hectare.",
    62: "Rapeseed & Mustard: Apply 50kg N + 50kg P2O5 per hectare.",
    63: "Peas (Vegetable): Apply 20kg N + 40kg P2O5 per hectare.",
    64: "Niger seed: Apply 25kg N + 25kg P2O5 per hectare.",
    65: "Bottle Gourd: Apply 50kg N + 50kg P2O5 + 50kg K2O per hectare.",
    66: "Varagu: Apply 25kg N + 20kg P2O5 per hectare.",
    67: "Garlic: Apply 50kg N + 50kg P2O5 + 50kg K2O per hectare.",
    68: "Ginger: Apply 50kg N + 50kg P2O5 + 50kg K2O per hectare.",
    69: "Oilseeds total: Apply 50kg N + 50kg P2O5 per hectare.",
    70: "Pulses total: Apply 20kg N + 40kg P2O5 per hectare.",
    71: "Jute: Apply 60kg N + 30kg P2O5 + 30kg K2O per hectare.",
    72: "Peas & beans (Pulses): Apply 20kg N + 40kg P2O5 per hectare.",
    73: "Blackgram: Apply 20kg N + 40kg P2O5 per hectare.",
    74: "Paddy: Apply 100kg N + 50kg P2O5 + 50kg K2O per hectare.",
    75: "Pineapple: Apply 100g NPK 10:10:20 per plant monthly.",
    76: "Barley: Apply 60kg N + 40kg P2O5 + 20kg K2O per hectare.",
    77: "Sannhamp: Apply 25kg N + 20kg P2O5 per hectare.",
    78: "Khesari: Apply 20kg N + 40kg P2O5 per hectare.",
    79: "Guar seed: Apply 25kg N + 25kg P2O5 per hectare.",
}


# ════════════════════════════════════════
#  HOME
# ════════════════════════════════════════
@app.route('/')
def index():
    return render_template('index.html')


# ════════════════════════════════════════
#  PREDICTION
# ════════════════════════════════════════
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        crop_year    = int(request.form['crop_year'])
        crop         = int(request.form['crop'])
        temperature  = float(request.form['temperature'])
        humidity     = float(request.form['humidity'])
        soil_moisture = float(request.form['soil_moisture'])
        area         = float(request.form['area'])

        input_features = np.array([[crop_year, crop, temperature, humidity, soil_moisture, area]])
        prediction = model.predict(input_features)
        fertilizer = fertilizer_suggestions.get(crop, "No suggestion available for this crop.")

        return render_template('result.html',
                               prediction=round(float(prediction[0]), 2),
                               fertilizer=fertilizer)

    return render_template('prediction.html')


# ════════════════════════════════════════
#  LOGIN
# ════════════════════════════════════════
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('predict'))

    error = None
    if request.method == 'POST':
        email    = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')

        user = users_db.get(email)
        if user and user['password'] == password:
            session['user'] = email
            session['name'] = user['first_name']
            return redirect(url_for('predict'))
        else:
            error = "Invalid email or password. Please try again."

    return render_template('login.html', error=error)


# ════════════════════════════════════════
#  SIGN UP
# ════════════════════════════════════════
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if 'user' in session:
        return redirect(url_for('predict'))

    error = None
    if request.method == 'POST':
        first_name = request.form.get('first_name', '').strip()
        last_name  = request.form.get('last_name', '').strip()
        email      = request.form.get('email', '').strip().lower()
        password   = request.form.get('password', '')
        confirm    = request.form.get('confirm_password', '')
        state      = request.form.get('state', '')

        if not first_name or not last_name:
            error = "Please enter your full name."
        elif email in users_db:
            error = "An account with this email already exists. Please log in."
        elif len(password) < 8:
            error = "Password must be at least 8 characters long."
        elif password != confirm:
            error = "Passwords do not match. Please try again."
        else:
            users_db[email] = {
                'first_name': first_name,
                'last_name':  last_name,
                'password':   password,
                'state':      state,
            }
            session['user'] = email
            session['name'] = first_name
            return redirect(url_for('predict'))

    return render_template('signup.html', error=error)


# ════════════════════════════════════════
#  LOGOUT
# ════════════════════════════════════════
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# ════════════════════════════════════════
if __name__ == '__main__':
    app.run(debug=True)
