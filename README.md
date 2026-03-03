# 🚀 Resume Screening Automation using NLP

An intelligent system that automates **resume screening** and matches candidates with internship job descriptions using **Natural Language Processing (NLP)** and **Machine Learning**. This project reduces manual screening time and improves candidate shortlisting efficiency.

---

## 🎯 Objective

Manual resume screening is time-consuming and inconsistent.  
This project builds an automated pipeline that:

- Extracts meaningful information from resumes  
- Compares candidate profiles with job descriptions  
- Ranks the most suitable candidates  
- Displays results in an interactive web dashboard  

---

## 🧠 How It Works

1. **Load Data**: Resume dataset (`intern_resumes_sample.csv`) and job descriptions (`jobs.csv`)  
2. **Preprocess Text**: Clean resumes using spaCy (lemmatization, stopword removal)  
3. **Feature Extraction**: Convert text to TF-IDF vectors  
4. **Similarity Matching**: Compute cosine similarity between resumes and job descriptions  
5. **Candidate Ranking**: Rank candidates for each job role  
6. **Dashboard Visualization**: Display top candidates with similarity scores in Flask web app  

---

## ✨ Features

- Automated candidate shortlisting  
- NLP-based skill extraction  
- TF-IDF similarity matching  
- Candidate ranking system  
- Interactive web dashboard  
- Data visualization of top candidates  

---

## 🖥 Web Application Preview

### Home Page
Click **Run Matching** to start the automated screening process.

### Results Dashboard
- Displays top candidates per job  
- Shows similarity scores  
- Includes visual ranking charts  

---

## 🧰 Technology Stack

| Category | Tools |
|----------|------|
| Programming | Python |
| NLP | spaCy |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas |
| Visualization | Matplotlib |
| Web Framework | Flask |

---

## 📂 Project Structure


resume-screening-automation/
│
├── app.py
├── jobs.csv
├── intern_resumes_sample.csv
├── requirements.txt
├── README.md
│
├── notebook/
│ └── Resume_Screening.ipynb
│
├── templates/
│ ├── index.html
│ └── results.html
│
└── static/
└── style.css


---

## ⚙️ Installation Guide

1. **Clone Repository**

```bash
git clone <your-repo-link>
cd resume-screening-automation

Install Dependencies

pip install -r requirements.txt

Download spaCy English Model

python -m spacy download en_core_web_sm

Run Flask App

python app.py

Open Browser

http://127.0.0.1:5000

Click Run Matching to view results.

📊 Dataset Information

Resume dataset (intern_resumes_sample.csv)

Job descriptions (jobs.csv)

Note: A sample dataset is included for demonstration. Full dataset is not uploaded due to privacy and size constraints.

📈 Output

For each job role, the system produces:

Ranked candidate list

Similarity score

Visual comparison chart

🎓 Learning Outcomes

Applied NLP to real-world data

Implemented document similarity modeling

Built an end-to-end ML pipeline

Developed a deployable web application

Integrated ML results into a visual dashboard

🔮 Future Improvements

Support PDF resume uploads

Use BERT embeddings for higher accuracy

Deploy web app online

Add recruiter analytics dashboard

Multi-job batch matching

👨‍💻 Author

Sobaan
