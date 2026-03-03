🚀 Resume Screening Automation using NLP

An intelligent system that automatically matches resumes with internship job descriptions using Natural Language Processing (NLP) and Machine Learning similarity techniques.

This project demonstrates how organizations can automate candidate shortlisting and significantly reduce manual screening time.

🎯 Project Objective

Manual resume screening is time-consuming and inconsistent.
This project builds an automated pipeline that:

✅ Extracts meaningful information from resumes

✅ Compares candidate profiles with job descriptions

✅ Ranks the most suitable candidates

✅ Displays results in a web dashboard

🧠 How It Works

Resume Dataset → NLP Preprocessing → Feature Extraction → Similarity Matching → Ranking → Web Dashboard
Step-by-step pipeline:

1️⃣ Load resume dataset (CSV)

2️⃣ Clean and normalize text using spaCy

3️⃣ Convert text to numerical vectors using TF-IDF

4️⃣ Compute similarity between resumes and jobs

5️⃣ Rank top candidates per job

6️⃣ Visualize results in Flask web app


✨ Features

✔ Automated resume filtering

✔ NLP-based skill extraction

✔ TF-IDF similarity matching

✔ Candidate ranking system

✔ Interactive Flask dashboard

✔ Data visualization of top candidates

✔ Works on real-world resume dataset

🖥 Web Application Preview
Home Page

Click to run automated matching.

Results Dashboard

Displays:

Top candidates per job

Similarity scores

Visual ranking charts

🧰 Technologies Used
Category	Tools

Programming	Python

NLP	spaCy

Machine Learning	Scikit-learn

Data Processing	Pandas

Visualization	Matplotlib

Web Framework	Flask


📂 Project Structure
resume-screening-automation/
│
├── app.py

├── jobs.csv

├── intern_resumes_sample.csv

├── requirements.txt

├── README.md
│
├── notebook/
│   └── Resume_Screening.ipynb
│
├── templates/
│   ├── index.html
│   └── results.html
│
└── static/
    └── style.css
⚙️ Installation Guide
1️⃣ Clone Repository
git clone <your-repo-link>
cd resume-screening-automation
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Download NLP Model
python -m spacy download en_core_web_sm
4️⃣ Run Application
python app.py
5️⃣ Open Browser
http://127.0.0.1:5000

Click Run Matching to view results.

📊 Dataset Information

The system uses:

Resume dataset (CSV format)

Job descriptions dataset

To ensure privacy and repository size efficiency:
✔ A sample dataset is included

✔ Full dataset not uploaded

📈 Output Example

For each job role, the system produces:

✔ Ranked candidate list

✔ Similarity score

✔ Visual comparison chart

🎓 Learning Outcomes

Through this project:

✔ Applied NLP to real-world data

✔ Implemented document similarity modeling

✔ Built an end-to-end ML pipeline

✔ Developed a production-style web interface

✔ Practiced data-driven decision automation

🔮 Future Improvements

⬜ Support PDF resume uploads
⬜ Use BERT embeddings for better accuracy
⬜ Add skill extraction dashboard
⬜ Deploy web app online

⬜ Recruiter login system
