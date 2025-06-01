import os
import joblib
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Sample job profiles with associated skill sets (text)
job_profiles = [
    {
        "job_title": "Data Scientist",
        "skills": "Python, Machine Learning, Statistics, Data Analysis, SQL"
    },
    {
        "job_title": "Web Developer",
        "skills": "HTML, CSS, JavaScript, React, Node.js"
    },
    {
        "job_title": "Civil Services Officer",
        "skills": "Public Administration, Law, Current Affairs, Ethics"
    },
    {
        "job_title": "Graphic Designer",
        "skills": "Adobe Photoshop, Illustrator, Creativity, Typography"
    },
    {
        "job_title": "Medical Doctor",
        "skills": "Biology, Anatomy, Patient Care, Diagnosis"
    },
]

# Initialize sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Embed skills text
skills_texts = [profile["skills"] for profile in job_profiles]
embeddings = model.encode(skills_texts)

# Save embeddings and metadata
os.makedirs("app/models", exist_ok=True)
joblib.dump({
    "job_profiles": job_profiles,
    "embeddings": embeddings
}, "app/models/skill_profiles.pkl")

print("✅ Skill profiles and embeddings saved.")
