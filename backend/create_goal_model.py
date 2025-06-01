import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample training data
texts = [
    "I love building robots and machines",
    "I'm interested in medicine and helping patients",
    "Business and marketing excite me",
    "I enjoy designing graphics and animations",
    "Teaching and mentoring is my passion",
    "I want to serve the country and join civil services",
]

labels = [
    "Engineering",
    "Medical",
    "Commerce",
    "Design",
    "Education",
    "Civil Services",
]

# Vectorize the text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train the model
model = MultinomialNB()
model.fit(X, labels)

# Save both model and vectorizer
os.makedirs("app/models", exist_ok=True)
joblib.dump(model, "app/models/goal_model.pkl")
joblib.dump(vectorizer, "app/models/goal_vectorizer.pkl")

print("✅ Goal extraction model and vectorizer saved.")
