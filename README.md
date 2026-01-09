
🏠 Real Estate Price Prediction
Machine Learning + Django + MySQL + Bootstrap UI

A complete end-to-end Real Estate Price Prediction System that uses machine learning to predict house prices based on key property features.
Built with Python, Scikit-Learn, Django, MySQL, and a modern glass-morphism UI with Bootstrap.

FEATURES:
- Machine Learning Model (Linear Regression)
- Real-time prediction using Django
- Stores prediction history in MySQL
- Modern UI with animations & glass effect
- Bootstrap 5, custom CSS, and background image
- ML pipeline with OneHotEncoder & ColumnTransformer

PROJECT STRUCTURE:
real_estate_price_prediction/
│
├── ml_model/
│   ├── data/Housing.csv
│   ├── train_model.py
│   └── house_price_model.pkl
│
├── realestate_project/
│   ├── manage.py
│   ├── realestate_project/
│   └── prediction_app/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── templates/
│       │   ├── input_form.html
│       │   └── result.html
│       ├── static/
│       │   ├── style.css
│       │   └── images/
│       └── house_price_model.pkl
│
└── README.md

INSTALLATION:
1. Clone the repo:
   git clone https://github.com/YOUR-USERNAME/Real_Estate_Price_Prediction.git
   cd Real_Estate_Price_Prediction

2. Create virtual environment:
   python -m venv env
   env\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Train ML model:
   cd ml_model
   python train_model.py

5. Create MySQL DB:
   CREATE DATABASE realestate_db;

6. Run migrations:
   python manage.py makemigrations
   python manage.py migrate

7. Start server:
   python manage.py runserver

8. Open in browser:
   http://127.0.0.1:8000/

AUTHOR:
Sarvesh
GitHub: https://github.com/sarveshpawar004
