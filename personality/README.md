# 🧠 Personality Prediction AI

![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

A machine learning-powered web application that predicts your personality type (Introvert vs. Extrovert) based on behavioral inputs. Features a premium Glassmorphism UI, interactive data visualization, and prediction history tracking.

## ✨ Features
*   **🤖 AI-Powered**: Uses a trained Random Forest Classifier to predict personality.
*   **🎨 Premium UI**: Modern Glassmorphism design with smooth animations and gradients.
*   **📊 Data Visualization**: Interactive Radar Charts to visualize your personality traits.
*   **📜 History Tracking**: Automatically saves and displays your recent prediction results.
*   **📱 Responsive**: Fully optimized for mobile and desktop devices.

## 🛠️ Tech Stack
*   **Backend**: Django 5, Python 3.11
*   **ML Engine**: Scikit-Learn, Pandas, NumPy
*   **Frontend**: HTML5, CSS3, Bootstrap 5, Chart.js
*   **Database**: SQLite (Dev), manageable via Django ORM

## 🚀 How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone https://github.com/YOUR_USERNAME/personality-prediction-app.git
    cd personality-prediction-app
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Migrations**
    ```bash
    python manage.py migrate
    ```

4.  **Train the Model (First time only)**
    ```bash
    python personality/train_model.py
    ```

5.  **Start the Server**
    ```bash
    python manage.py runserver
    ```

6.  Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## 🤝 Contributing
Contributions are welcome! Feel free to submit a Pull Request.
