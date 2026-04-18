# 📊 Sentiment Analysis Project

A Machine Learning project that predicts the sentiment of user reviews (Positive/Negative) using Natural Language Processing (NLP) techniques.

---

## 🚀 Project Overview

This project focuses on analyzing textual data and classifying it into sentiments using a trained model. It demonstrates the complete Data Science workflow:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature extraction using TF-IDF
* Model training using LinearSVC
* Deployment using Streamlit

---

## 🛠️ Technologies Used

* Python 
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* Joblib

---

## 📂 Project Structure

```
Sentiment-Analysis_Project/
│
├── deployment.py                 # Streamlit app for deployment
├── Sentiment_Analysis.ipynb     # Jupyter notebook (model training & EDA)
├── linearSVC_model.joblib       # Trained ML model
├── tfidf_vectorizer.joblib      # TF-IDF vectorizer
├── P597 DATASET.xlsx            # Dataset used for training
│
├── README.md                    # Project documentation
└── .gitignore                   # Ignored files
```


---

## ⚙️ How It Works

1. Text data is cleaned and preprocessed
2. TF-IDF converts text into numerical features
3. LinearSVC model is trained on labeled data
4. The model predicts sentiment for new input text

---

## 💻 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/s-abdul-02/Sentiment-Analysis_Project.git
cd Sentiment-Analysis-Project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run deployment.py
```

---

## 📈 Features

* Real-time sentiment prediction
* Clean and interactive UI using Streamlit
* Pre-trained machine learning model
* Easy to extend for other NLP tasks

---

## 🧠 Model Details

* Algorithm: Linear Support Vector Classifier (LinearSVC)
* Feature Extraction: TF-IDF Vectorizer
* Library: Scikit-learn

---

## 📊 Future Improvements

* Add deep learning models (LSTM, BERT)
* Improve accuracy with hyperparameter tuning
* Deploy on cloud platforms (AWS/Heroku)
* Add multi-class sentiment (Positive, Negative, Neutral)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 📬 Contact

For any queries or collaboration:

* GitHub: https://github.com/s-abdul-02

---

⭐ If you like this project, give it a star!
