import pandas as pd
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nlp = spacy.load("en_core_web_sm")

resumes = pd.read_csv("Resume.csv")
print("Resumes Loaded:", resumes.shape)
resumes.head()

jobs = pd.read_csv("jobs.csv")
print("Job Descriptions Loaded:", jobs.shape)
jobs.head()

resumes = resumes.rename(columns={
    "ID": "Candidate_ID",
    "Resume_str": "Resume_Text"
})

resumes = resumes[["Candidate_ID", "Resume_Text"]]
resumes.head()

def extract_keywords(text):
    doc = nlp(str(text).lower())
    keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(keywords)

resumes['Cleaned_Resume'] = resumes['Resume_Text'].apply(extract_keywords)
jobs['Cleaned_Description'] = jobs['Description'].apply(extract_keywords)

resumes.head(), jobs.head()

all_texts = pd.concat([resumes['Cleaned_Resume'], jobs['Cleaned_Description']])

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_texts)

resume_vectors = tfidf_matrix[:len(resumes)]
job_vectors = tfidf_matrix[len(resumes):]

similarity_matrix = cosine_similarity(resume_vectors, job_vectors)
similarity_matrix

results = []

for job_index, job in jobs.iterrows():
    sim_scores = similarity_matrix[:, job_index]

    ranked_candidates = resumes[["Candidate_ID"]].copy()
    ranked_candidates["Similarity_Score"] = sim_scores
    ranked_candidates = ranked_candidates.sort_values(
        by="Similarity_Score",
        ascending=False
    )

    results.append({
        "Job_ID": job["Job_ID"],
        "Job_Title": job["Title"],
        "Top_Candidates": ranked_candidates.head(5)
    })

results

for job in results:
    print("\n==============================")
    print("Job:", job["Job_Title"])
    print("==============================")
    print(job["Top_Candidates"])

import matplotlib.pyplot as plt

for job in results:
    df = job["Top_Candidates"]

    names = df["Candidate_ID"].astype(str)
    scores = df["Similarity_Score"]

    plt.figure(figsize=(8,5))
    plt.barh(names, scores)
    plt.xlabel("Similarity Score")
    plt.title(f"Top Candidates for {job['Job_Title']}")
    plt.gca().invert_yaxis()
    plt.show()

final_rows = []

for job in results:
    for _, row in job["Top_Candidates"].iterrows():
        final_rows.append({
            "Job_ID": job["Job_ID"],
            "Job_Title": job["Job_Title"],
            "Candidate_ID": row["Candidate_ID"],
            "Similarity_Score": row["Similarity_Score"]
        })

final_df = pd.DataFrame(final_rows)
final_df.to_csv("ranked_candidates.csv", index=False)

print("Saved as ranked_candidates.csv")
final_df.head()