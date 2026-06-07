# 🛡️ Cyberbullying Detection System

An AI-powered web application that detects cyberbullying content in text using Machine Learning and Natural Language Processing (NLP). The system helps identify harmful online messages and promotes safer digital communication.

---

## 🚀 Project Overview

Cyberbullying has become a significant challenge across social media and online platforms. This project leverages Machine Learning techniques to analyze user-generated text and classify whether the content is cyberbullying or non-cyberbullying.

The application provides a user-friendly web interface built with Django, allowing users to submit text and instantly receive predictions.

---

## ✨ Features

✅ User Registration & Login

✅ Admin Dashboard

✅ Cyberbullying Text Detection

✅ Machine Learning-Based Classification

✅ Dataset Processing & Analysis

✅ Secure User Management

✅ Interactive Web Interface

---

## 🏗️ System Architecture

User Input → Text Preprocessing → Feature Extraction → ML Model → Prediction Result

---

## 🛠️ Technologies Used

### Backend

* Python
* Django

### Machine Learning

* Scikit-Learn
* Natural Language Processing (NLP)

### Data Processing

* Pandas
* NumPy

### Frontend

* HTML
* CSS
* Bootstrap
* JavaScript

### Database

* SQLite

---

## 📂 Project Structure

```text
Cyberbullying/
│
├── Admin/
├── User/
├── Cyberbullying/
├── templates/
├── static/
├── Cyberbullying.csv
├── manage.py
└── README.md
```

---

## 📊 Dataset

The model is trained using a cyberbullying dataset containing text samples categorized as:

* Cyberbullying
* Non-Cyberbullying

The dataset undergoes preprocessing, cleaning, and feature extraction before model training.

---

## 🔍 Machine Learning Workflow

### Data Collection

* Load cyberbullying dataset

### Data Preprocessing

* Text cleaning
* Lowercasing
* Tokenization
* Stop-word removal

### Feature Engineering

* TF-IDF Vectorization

### Model Training

* Train classification model

### Prediction

* Classify user-entered text as:

  * Cyberbullying
  * Non-Cyberbullying

---

## ⚙️ Installation Guide

### Clone Repository

```bash
git clone https://github.com/shreyabn12/Cyberbullying-Detection-System.git
```

### Navigate to Project

```bash
cd Cyberbullying-Detection-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 🎯 Future Enhancements

* Deep Learning Models
* Transformer-Based Detection
* Real-Time Social Media Monitoring
* Multi-Language Support
* Sentiment Analysis Integration
* Deployment on Cloud Platforms

---



## 👩‍💻 Author

**Shreya B N**


Interested in:

* Data Science
* Machine Learning
* Generative AI
* Natural Language Processing

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.
