# app/models/skill_mapper.py

from sentence_transformers import SentenceTransformer, util

class SkillMapper:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        # Example industry skill profiles (can be expanded)
        self.industry_profiles = {
            "software developer": ["programming", "java", "python", "data structures", "algorithms"],
            "data scientist": ["machine learning", "python", "statistics", "data analysis", "deep learning"],
            "civil engineer": ["autocad", "structural analysis", "project management"],
            "doctor": ["biology", "anatomy", "pharmacology"],
            "accountant": ["accounting", "finance", "taxation"],
        }
        # Precompute embeddings
        self.profile_embeddings = {}
        for profile, skills in self.industry_profiles.items():
            combined = " ".join(skills)
            self.profile_embeddings[profile] = self.model.encode(combined, convert_to_tensor=True)

    def map_skills(self, user_skills):
        user_embedding = self.model.encode(" ".join(user_skills), convert_to_tensor=True)
        similarities = {}
        for profile, embedding in self.profile_embeddings.items():
            sim = util.pytorch_cos_sim(user_embedding, embedding)[0][0].item()
            similarities[profile] = sim
        # Sort profiles by similarity desc
        sorted_profiles = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
        # Return top 3 profiles with score
        return [{"profile": p, "score": s} for p, s in sorted_profiles[:3]]
