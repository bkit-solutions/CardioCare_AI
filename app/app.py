from flask import Flask, render_template, request, send_file, session
import pickle
import numpy as np
import pandas as pd
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

app = Flask(__name__)
app.secret_key = "cardiocare_ai_secret_key"  # required for session

# ================= LOAD MODELS =================

with open("../models/hybrid_heart_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("../models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("../models/feature_columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)

# ================= RISK LOGIC =================

def classify_risk(prob):
    if prob < 0.35:
        return "Low Risk"
    elif prob < 0.65:
        return "Moderate Risk"
    else:
        return "High Risk"


def get_recommendation(risk):
    recommendations = {
        "Low Risk": "Maintain a healthy lifestyle with balanced diet and regular exercise.",
        "Moderate Risk": "Consult a cardiologist and monitor blood pressure and cholesterol.",
        "High Risk": "Immediate medical attention recommended. Follow prescribed treatment."
    }
    return recommendations.get(risk, "Consult a doctor for detailed recommendations.")

# ================= ROUTES =================

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/analysis", methods=["GET", "POST"])
def analysis():
    if request.method == "POST":

        # -------- STEP 1: RAW INPUT --------
        raw_input = {
            "age": float(request.form["age"]),
            "trestbps": float(request.form["trestbps"]),
            "chol": float(request.form["chol"]),
            "thalch": float(request.form["thalch"]),
            "oldpeak": float(request.form["oldpeak"]),
            "ca": float(request.form["ca"]),

            "sex": "Male" if int(request.form["sex"]) == 1 else "Female",
            "fbs": True if int(request.form["fbs"]) == 1 else False,
            "exang": True if int(request.form["exang"]) == 1 else False,

            "cp": request.form["cp"],
            "restecg": request.form["restecg"],
            "slope": request.form["slope"],
            "thal": request.form["thal"]
        }

        # -------- STEP 2: MAP CATEGORIES --------
        cp_map = {
            "0": "typical angina",
            "1": "atypical angina",
            "2": "non-anginal",
            "3": "asymptomatic"
        }
        restecg_map = {
            "0": "normal",
            "1": "st-t abnormality",
            "2": "lv hypertrophy"
        }
        slope_map = {
            "0": "downsloping",
            "1": "flat",
            "2": "upsloping"
        }
        thal_map = {
            "0": "normal",
            "1": "normal",
            "2": "fixed defect",
            "3": "reversable defect"
        }

        raw_input["cp"] = cp_map.get(raw_input["cp"], "asymptomatic")
        raw_input["restecg"] = restecg_map.get(raw_input["restecg"], "normal")
        raw_input["slope"] = slope_map.get(raw_input["slope"], "flat")
        raw_input["thal"] = thal_map.get(raw_input["thal"], "normal")

        # -------- STEP 3: DATAFRAME --------
        input_df = pd.DataFrame([raw_input])

        # -------- STEP 4: ONE-HOT ENCODE --------
        input_encoded = pd.get_dummies(input_df, drop_first=True)

        # -------- STEP 5: ALIGN FEATURES --------
        input_encoded = input_encoded.reindex(
            columns=feature_columns, fill_value=0
        )

        # -------- STEP 6: SCALE --------
        X_scaled = scaler.transform(input_encoded)

        # -------- STEP 7: PREDICT --------
        prob = model.predict_proba(X_scaled)[0][1]
        risk = classify_risk(prob)
        recommendation = get_recommendation(risk)

        # -------- STORE IN SESSION (FOR PDF) --------
        session["risk"] = risk
        session["probability"] = round(prob * 100, 2)
        session["recommendation"] = recommendation

        return render_template(
            "result.html",
            probability=session["probability"],
            risk=risk,
            recommendation=recommendation
        )

    return render_template("analysis.html")


# ================= PDF REPORT =================

@app.route("/download-report")
def download_report():
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    # Title
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, 800, "CardioCare AI - Heart Disease Risk Report")

    # Body
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 760, "Hybrid Machine Learning Clinical Decision Support System")

    pdf.drawString(50, 720, f"Risk Level: {session.get('risk', 'N/A')}")
    pdf.drawString(50, 700, f"Risk Probability: {session.get('probability', 'N/A')}%")

    pdf.drawString(50, 660, "Clinical Recommendation:")
    pdf.drawString(60, 640, session.get("recommendation", "N/A"))

    pdf.drawString(50, 600, "Model Used:")
    pdf.drawString(60, 580, "Logistic Regression + Random Forest + Gradient Boosting")

    pdf.drawString(50, 540, "Note:")
    pdf.drawString(60, 520, "This report is generated for educational purposes only.")

    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name="CardioCare_AI_Report.pdf",
        mimetype="application/pdf"
    )


# ================= RUN =================

if __name__ == "__main__":
    app.run(debug=True)
