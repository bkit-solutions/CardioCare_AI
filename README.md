
# ❤️ CardioCare AI — Hybrid Heart Disease Risk Prediction

CardioCare AI is a **Flask-based Hybrid Machine Learning Clinical Decision Support System**
designed to **predict heart disease risk** using patient clinical parameters.

The project combines multiple machine learning models to provide a **robust risk probability,
risk classification, and clinical recommendation**, presented through a **modern and interactive web UI**.

⚠️ **Academic Use Only**  
This system is developed strictly for **educational and final-year B.Tech project demonstration purposes**.
It is **not a medical diagnosis tool**.

---

## 🚀 Project Overview

CardioCare AI takes patient clinical inputs such as age, blood pressure, cholesterol levels,
ECG results, exercise-induced angina, and vessel conditions, then:

- Preprocesses and scales the data
- Uses a **Hybrid Ensemble ML Model**
- Predicts **heart disease risk probability**
- Classifies risk as **Low / Moderate / High**
- Provides **clinical recommendations**
- Generates a **downloadable PDF report**
- Includes an **interactive assistant chatbot** for explanation

---

## ✨ Key Features

- 🧠 Hybrid Machine Learning Ensemble  
- 📊 Risk Probability Visualization  
- 🩺 Risk Classification (Low / Moderate / High)  
- 📄 Downloadable PDF Medical Report  
- 💬 Interactive AI Assistant Chatbot  
- ⚡ Instant Prediction  
- 🔐 Offline & Secure (No data persistence)  
- 🎓 Final Year B.Tech Ready UI  

---

## 🛠️ Technology Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript  
- Jinja2 (Flask Templates)

### Backend
- Python (Flask)  
- Scikit-learn  
- NumPy  
- Pandas  

### ML Models
- Logistic Regression  
- Random Forest  
- Gradient Boosting  

---

## 📁 Project Structure

```
CardioCare_AI/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   │
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │       └── main.js
│   │
│   └── templates/
│       ├── base.html
│       ├── home.html
│       ├── analysis.html
│       └── result.html
│
├── models/
│   ├── hybrid_heart_model.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
│
├── data/
├── notebooks/
├── venv/
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone <your-repository-url>
cd Heart_Disease
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
python app/app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 How CardioCare AI Works

1. User enters clinical parameters  
2. Data is preprocessed & scaled  
3. Hybrid ML ensemble predicts risk probability  
4. Risk is classified into categories  
5. Recommendation is generated  
6. User can download a PDF report  
7. Chatbot explains results interactively  

---

## 📊 Risk Classification Logic

| Risk Level | Probability Range |
|----------|------------------|
| Low Risk | < 35% |
| Moderate Risk | 35% – 65% |
| High Risk | > 65% |

---

## 📄 PDF Report

The system generates a structured PDF report containing:
- Risk level
- Risk probability
- Model description
- Clinical recommendation
- Academic disclaimer

---

## 🤖 AI Assistant Chatbot

The chatbot can explain:
- Risk meaning
- Model architecture
- Recommendations
- Project overview

This improves **user understanding** and **presentation value**.

---

## 🧪 Academic Disclaimer

⚠️ **Disclaimer:**  
This project is intended **only for academic, educational, and demonstration purposes**.
It must **not** be used for real-world medical diagnosis or treatment.

---

## 🔮 Future Enhancements

- Explainable AI (XAI) feature importance  
- Patient-wise history tracking  
- Doctor dashboard  
- Model accuracy charts  
- Cloud deployment  
- Mobile-first UI  

---

## 📜 License

MIT License  
Free to use for academic and educational purposes.

---

## 👨‍💻 Contributors

**CardioCare AI Team**  
Final Year B.Tech Project — 2026  

AI / ML • Web Development • Data Science
