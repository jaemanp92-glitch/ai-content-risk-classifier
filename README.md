# AI Content Risk Classifier

## 📌 Overview
This project is a machine learning model that classifies toxic comments using NLP techniques.

## 🧠 What I did
- Preprocessed text data from Kaggle dataset
- Converted text into numerical vectors using TF-IDF
- Trained Logistic Regression model
- Handled class imbalance using class_weight
- Evaluated model using accuracy, F1-score, confusion matrix

## 📊 Result
- Accuracy: ~93%
- Improved recall for toxic class using balanced model

## 🛠 Tech Stack
- Python
- Pandas
- Scikit-learn
- NLP (TF-IDF)

## 📁 Dataset
Kaggle - Toxic Comment Classification Challenge

## 🚀 Future Improvements
- Try deep learning (LSTM, BERT)
- Improve precision for toxic class
- Deploy as web service

## 🛡 Policy Decision System

In addition to the machine learning classifier, I designed a rule-based policy decision system that simulates real-world content moderation workflows.

### Example

Input:
"I will kill you"

Output:
- Violation: YES  
- Policy: Threat  
- Action: Remove  
- Reason: Direct threat detected  

### Purpose

This system demonstrates how moderation decisions are not only based on model predictions, but also on policy logic and enforcement rules.
