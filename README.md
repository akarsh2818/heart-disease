# ❤️ Heart Disease Prediction App

This Streamlit web app predicts the **risk of heart disease** based on user-provided health information using a trained machine learning model.

---

## 🚀 Live App

👉 [Click here to try the app](https://heartdiseasecheck.streamlit.app/)

---

## 🧠 How It Works

The app uses a **Logistic Regression model** trained on heart health data. Users input values like age, cholesterol, and chest pain type, and the app predicts:

✅ **Low Risk**  
⚠️ **High Risk**

---

## 📓 Model Training

The machine learning model was built and trained in this notebook:

📄 [`heart.ipynb`](heart.ipynb)

It includes:

- Data preprocessing (encoding, scaling)
- Training (Logistic Regression, KNN, etc.)
- Evaluation (Accuracy, F1 Score)
- Export of:
  - `Logistic_regression_heart.pkl`
  - `scaler.pkl`
  - `columns.pkl`

---

## 📂 Project Structure

heart-disease-predictor/
│
├── app.py # Streamlit frontend app
├── heart.ipynb # Model training notebook
├── scaler.pkl # StandardScaler object
├── Logistic_regression_heart.pkl # Trained ML model
├── columns.pkl # Expected input feature names
├── requirements.txt # Required packages for deployment
└── README.md # This file

yaml
Copy
Edit

---

## ⚙️ Installation & Running Locally

```bash
git clone https://github.com/<your-username>/heart-disease-predictor.git
cd heart-disease-predictor
pip install -r requirements.txt
streamlit run app.py
📦 Deploy to Streamlit Cloud
Upload this project to GitHub (including .pkl files).

Go to https://streamlit.io/cloud

Click "New app" → Select repo & app.py

Done! 🎉

🛠 Tech Stack
Python 🐍

Streamlit 📊

scikit-learn 🤖

joblib 🧪

pandas 🐼

Jupyter Notebook 📓

🙋‍♂️ About the Author
Made with ❤️ by Akarsh Jha
🔗 Deployed App
