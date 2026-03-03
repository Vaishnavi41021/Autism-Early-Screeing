# Autism-Early-Screeing

---

# 🧠 Autism Early Screening System

## 📌 Project Overview

The **Autism Early Screening System** is a web-based application designed to help parents perform an early behavioral screening for Autism Spectrum Disorder (ASD) in children.

The system collects responses from parents through a structured questionnaire, calculates a screening score using a rule-based algorithm, and classifies the child’s autism risk level as:

* Low Risk
* Medium Risk
* High Risk

⚠️ This tool is intended for **early screening purposes only** and does not provide a medical diagnosis.

---

## 🎯 Objectives

* Provide an easy-to-use early screening tool for parents
* Digitize autism behavioral questionnaires
* Automatically calculate screening score
* Classify autism risk level
* Store screening records in a database
* Display results in a clean dashboard interface

---

## 🧩 Features

* 📝 Parent-based questionnaire form
* 📊 Automatic score calculation
* ⚠️ Risk level classification (Low / Medium / High)
* 💾 SQLite database integration
* 📋 Stored screening records display
* 🎨 Modern UI with responsive layout

---

## 🛠 Technologies Used

### 💻 Frontend

* HTML5
* CSS3
* Jinja2 (Flask templating)

### ⚙️ Backend

* Python 3.x
* Flask Framework

### 🗄 Database

* SQLite3

---

## 🧠 Algorithm Used

The system uses a **Rule-Based Decision Scoring Algorithm**:

1. Each “Yes” response = 1 point
2. Each “No” response = 0 points
3. Total score is calculated
4. Risk level is determined based on predefined thresholds:

| Score Range | Risk Level  |
| ----------- | ----------- |
| 0 – 2       | Low Risk    |
| 3 – 5       | Medium Risk |
| 6+          | High Risk   |

Time Complexity: O(n), where n = number of questions.

---

## 🗂 Project Structure

```
Autism-Screening/
│
├── app.py
├── autism.db
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   └── css/
│       └── clinical.css
│
└── README.md
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
https://github.com/Vaishnavi41021/Autism-Early-Screeing.git
```

2. Navigate to the project folder:

```
cd autism-screening
```

3. Install dependencies:

```
pip install flask
```

4. Run the application:

```
python app.py
```

5. Open browser:

```
http://127.0.0.1:5000
```

---

## 💻 System Requirements

* Python 3.10 or higher
* 8 GB RAM (recommended)
* Modern web browser (Chrome, Edge, Firefox)
* Windows / macOS / Linux

---

## 🔮 Future Enhancements

* Machine Learning–based autism prediction model
* Risk visualization graph
* PDF report generation
* Admin dashboard
* Secure login system
* Cloud database integration

---

## ⚠️ Disclaimer

This system is designed for **early screening assistance only**.
It does not replace professional medical diagnosis or clinical evaluation.
Parents are advised to consult a qualified healthcare professional for proper assessment.

---

## 👩‍💻 Developed By

Aelpula Vaishnavi
2026
