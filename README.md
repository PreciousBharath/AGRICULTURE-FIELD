<div align="center">
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=800&size=40&duration=3500&pause=1500&color=a8e063&center=true&vCenter=true&width=900&height=70&lines=%F0%9F%8C%BE%20AgriPredict" alt="AgriPredict"/>

<b><i>Smart Crop Production Prediction with ML & Deep Learning</i></b>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=36BCF7&center=true&vCenter=true&width=700&lines=%F0%9F%8C%B1%20Predict%20crop%20production;%F0%9F%A4%96%20ML%20%2B%20Deep%20Neural%20Network;%F0%9F%A7%91%E2%80%8D%F0%9F%8C%BE%20Built%20for%20smarter%20farming" alt="Typing SVG" />

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow"/> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="scikit-learn"/> <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas"/> <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter"/> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5"/> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3"/>

<img src="https://img.shields.io/github/stars/PreciousBharath/AGRICULTURE-FIELD?style=social" alt="stars"/> <img src="https://img.shields.io/github/forks/PreciousBharath/AGRICULTURE-FIELD?style=social" alt="forks"/> <img src="https://img.shields.io/github/last-commit/PreciousBharath/AGRICULTURE-FIELD?style=flat-square&color=blueviolet" alt="last commit"/> <img src="https://img.shields.io/github/repo-size/PreciousBharath/AGRICULTURE-FIELD?style=flat-square&color=success" alt="repo size"/>
</div>

---

## 🌾 About the Project

**AgriPredict** is a machine-learning web application that analyses agricultural field data and predicts **crop production** from inputs such as state, district, season, crop and area. It combines a classical ML model with a **Deep Neural Network (DNN)** and serves predictions through a clean Flask web interface with user login and sign-up.

## ✨ Key Features

- 🔐 User **sign-up / login** before accessing predictions
- 📊 Trained on a real **crop production dataset** (`Crop Prediction dataset.csv`)
- 🧠 Dual models — `model.pkl` (ML) and `dnn_model.h5` (Keras DNN)
- ⚡ Instant prediction results on a dedicated result page
- 📓 Full EDA + training workflow in `crop_production.ipynb`

## 🧠 How It Works

```mermaid
flowchart LR
A["🧑‍🌾 Farmer Input"] --> B["🧹 Preprocessing"] --> C{"🤖 ML / DNN Model"} --> D["🌾 Predicted Production"]
```

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3 |
| Data & ML | Pandas · NumPy · scikit-learn |
| Notebook | Jupyter |
| Web App | Flask + Jinja2 templates |
| Frontend | HTML5 · CSS3 |
| Deep Learning | TensorFlow / Keras (DNN) |

## 📂 Project Structure

```text
agripredict_updated/
├── app.py                     # Flask application
├── crop_production.ipynb      # EDA + model training
├── Crop Prediction dataset.csv
├── model.pkl                  # ML model
├── dnn_model.h5               # Deep neural network
├── static/css/agri.css
└── templates/  (index, login, signup, prediction, result)
```

## 🚀 Getting Started

```bash
git clone https://github.com/PreciousBharath/AGRICULTURE-FIELD.git
cd "AGRICULTURE-FIELD/agripredict_updated-20260416T074421Z-3-001/agripredict_updated"
pip install flask pandas numpy scikit-learn tensorflow
python app.py
# open http://127.0.0.1:5000
```

## 🤝 Contributing

Contributions, issues and feature requests are welcome! Feel free to ⭐ star the repo and open a pull request.

## 👨‍💻 Author

<div align="center">

**Bharath** — Software Developer · Project Engineer · Technical Trainer

<a href="https://github.com/PreciousBharath"><img src="https://img.shields.io/badge/GitHub-PreciousBharath-181717?style=for-the-badge&logo=github"/></a>
<a href="https://linkedin.com/in/connectbharath"><img src="https://img.shields.io/badge/LinkedIn-connectbharath-0A66C2?style=for-the-badge&logo=linkedin"/></a>

### 🍔 EAT · 😴 SLEEP · 💻 CODE · 🔁 REPEAT

⭐ **If you found this project useful, give it a star!** ⭐

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" width="100%"/>

</div>
