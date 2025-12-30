# Machine Learning Approach for Employee Performance Prediction
# Youtube link: https://youtu.be/C8UCnikT4lQ

This project presents a **Machine Learning-based Employee Productivity Prediction System** that evaluates workforce productivity using historical operational and behavioral factors.

The system predicts whether an employee is:

- Low Productive
- Medium Productive
- Highly Productive

It also provides interactive visual dashboards to support performance analysis and HR decision-making.

---

## 🎯 Objectives

- Predict employee productivity using machine learning  
- Identify key workforce performance factors  
- Support HR & management in productivity monitoring  
- Enable data-driven decision-making  
- Reduce productivity loss due to idle/over-time  
- Detect early risk of under-performance  

---

## 🧩 Problem Statement

Organizations often face:

- Subjective/manual productivity evaluation
- Absence of predictive workforce analytics
- Difficulty in detecting performance decline early
- Lack of real-time productivity indicators

This project introduces an **automated ML-based productivity prediction system** that analyzes key performance parameters and produces actionable insights.

---

## 🧠 Machine Learning Approach — Pipeline

The system follows a standard ML pipeline:

1. Data Collection  
2. Data Pre-processing  
3. Feature Engineering & Selection  
4. Model Training  
5. Performance Prediction  
6. Productivity Categorization  
7. Visualization & Dashboard Analytics  

---

## 🛠 System Architecture (Conceptual Flow)

User Input Form
↓
Data Pre-Processing
↓
ML Model Prediction
↓
Productivity Classification
↓
Dashboard Visualization


The model evaluates:

- Department-wise productivity behavior  
- Time & seasonal variations  
- Workload cycles  
- Historical performance indicators  

Employee_Performance_Prediction_Project/
│
├── Dataset/
│   └── garments_worker_productivity.csv
│
├── Training Files/
│   ├── Employee_Prediction.ipynb
│   ├── gwp.pkl
│   ├── mcle.pkl
│   └── .ipynb_checkpoints/
│
├── IBM Files/
│   ├── gwp.pkl
│   └── xgb_gwp.tgz
│
├── Flask/
│   ├── app.py
│   ├── gwp.pkl
│   └── templates/
│       ├── home.html
│       ├── predict.html
│       ├── submit.html
│       └── about.html
│
└── README.md

---

## 🌐 Web Application Implementation

**Framework:** Flask

flask
numpy
pandas
scikit-learn
pickle-mixin
gunicorn


### Frontend

- HTML  
- CSS  
- Bootstrap  
- Chart.js (Visualization)

### Backend

- Flask  
- NumPy  
- Pickle (Model Loading)

The trained ML model is executed via the `submit()` function and outputs are displayed through a performance dashboard.

---

## 📊 Performance Visualization Dashboard

The system includes multiple visual analytics such as:

- Bar Chart — Target vs Predicted Productivity  
- Line Chart — Performance Trend  
- Pie Chart — Idle Time vs Overtime Ratio  
- Stacked Area Chart — Contribution Factors  
- Stacked Column Chart — Productivity Comparison  
- Radar Chart — Skill / Efficiency Profile  
- Workforce Distribution Charts  

These charts help:

- HR Managers monitor productivity
- Supervisors identify workforce gaps
- Organizations detect process bottlenecks


<img width="1919" height="965" alt="Screenshot 2025-12-30 110307" src="https://github.com/user-attachments/assets/367fa891-c64e-4966-842f-041b82eb2299" />

<img width="1919" height="973" alt="Screenshot 2025-12-30 120244" src="https://github.com/user-attachments/assets/d1401da2-a64a-496f-9043-68a2585d29bf" />

<img width="1919" height="962" alt="Screenshot 2025-12-30 112706" src="https://github.com/user-attachments/assets/542f9fd3-766d-4706-b4be-f2d9ac537903" />

<img width="1919" height="973" alt="Screenshot 2025-12-30 113633" src="https://github.com/user-attachments/assets/68086814-f10e-42e8-8657-08ed42918f3a" />


---


## 🚀 Future Enhancements

- Deep-Learning based productivity modeling  
- Real-time productivity monitoring dashboard  
- Employee behavior & sentiment analytics  
- Predictive absenteeism modeling  
- HR decision-support integration  

---

## 🏁 Conclusion

The Employee Productivity Prediction System:

- Analyzes key performance indicators  
- Predicts productivity classification  
- Supports management decision-making  
- Enhances workforce efficiency  

It demonstrates how **machine learning & predictive analytics improve productivity assessment.**

---

## 👤 Author

**Angothu Adhisheshu**  
Machine Learning Research & Development

Github link:- https://github.com/Adhisheshu1210/
---

© 2025 — Machine Learning Approach for Employee Performance Prediction  
All Rights Reserved
