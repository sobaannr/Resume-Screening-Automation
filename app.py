from flask import Flask, render_template
import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(str(text).lower())
    keywords = [
        token.lemma_
        for token in doc
        if token.is_alpha and not token.is_stop
    ]
    return " ".join(keywords)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/match")
def match():

    resumes_df = pd.read_csv("Resume.csv")

    resumes_df = resumes_df.rename(columns={
        "ID": "Candidate_ID",
        "Resume_str": "Resume_Text"
    })

    resumes_df = resumes_df[["Candidate_ID", "Resume_Text"]]

    jobs_df = pd.read_csv("jobs.csv")

    resumes_df["Cleaned_Resume"] = resumes_df["Resume_Text"].apply(extract_keywords)
    jobs_df["Cleaned_Description"] = jobs_df["Description"].apply(extract_keywords)

    all_texts = pd.concat([
        resumes_df["Cleaned_Resume"],
        jobs_df["Cleaned_Description"]
    ])

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    resume_vectors = tfidf_matrix[:len(resumes_df)]
    job_vectors = tfidf_matrix[len(resumes_df):]

    similarity_matrix = cosine_similarity(resume_vectors, job_vectors)

    final_results = []

    for job_index, job in jobs_df.iterrows():
        sim_scores = similarity_matrix[:, job_index]

        ranked_candidates = resumes_df[["Candidate_ID"]].copy()
        ranked_candidates["Similarity_Score"] = sim_scores
        ranked_candidates = ranked_candidates.sort_values(
            by="Similarity_Score",
            ascending=False
        )

        top_candidates = ranked_candidates.head(5)

        names = top_candidates["Candidate_ID"].astype(str)
        scores = top_candidates["Similarity_Score"]

        plt.figure(figsize=(6,4))
        plt.barh(names, scores)
        plt.xlabel("Similarity Score")
        plt.title(f"Top Candidates for {job['Title']}")
        plt.gca().invert_yaxis()

        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plt.close()

        final_results.append({
            "Job_ID": job["Job_ID"],
            "Job_Title": job["Title"],
            "Top_Candidates": top_candidates.to_dict(orient="records"),
            "Plot_URL": plot_url
        })

    return render_template("results.html", results=final_results)


if __name__ == "__main__":
    app.run(debug=True)