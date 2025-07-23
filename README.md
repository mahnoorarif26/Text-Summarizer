# 📝Text Summarizer (Flask App)

A simple web-based **Text Summarization** tool built using Python, Flask, and Hugging Face Transformers. This app allows users to enter text and get a concise summary powered by state-of-the-art NLP models like bart.

---

## 🚀 Features

- 🔹 Summarizes any plain text input
- 🔹 Clean and minimal web interface using Flask + HTML/CSS
- 🔹 Powered by Hugging Face Transformers (`facebook/bart-large-cnn`)
- 🔹 Adjustable summary length parameters

---
```
## 🗂️ Project Structure

text-summarizer-app/
├── app.py # Flask backend
├── summarizer.py # Summarization logic using Transformers
├── templates/
│ └── index.html # Webpage template
├── static/
│ └── style.css # Basic CSS styling
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
## 📦 Installation

### 1️⃣ Clone the Repository
```
git clone https://github.com/mahnoorarif26/Text_Summarizer.git
cd text-summarizer-app
```

### 2️⃣ Install Required Packages
```
pip install -r requirements.txt
```
### ▶️ Running the App
Start the Flask server by running:
```
python app.py
```
Then open your browser and go to:
```
http://127.0.0.1:5000
```
 ## 🧠 Model Used
Model Name	Description
facebook/bart-large-cnn	Pretrained model for general-purpose summarization
