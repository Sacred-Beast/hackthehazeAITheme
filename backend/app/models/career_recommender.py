# app/models/career_recommender.py

class CareerRecommender:
    def __init__(self):
        # Map aptitude classes to career tiers (example)
        self.aptitude_map = {
            0: ["clerical jobs", "data entry", "customer support"],
            1: ["commerce related jobs", "teaching", "junior engineering roles"],
            2: ["engineering", "medical assistance", "data analyst"],
            3: ["software engineer", "doctor", "researcher", "civil services"],
        }

    def recommend(self, aptitude_class, goals, skill_profiles):
        recommendations = set()
        # Add aptitude based recommendations
        recommendations.update(self.aptitude_map.get(aptitude_class, []))

        # Add goal based recommendations
        for goal in goals:
            recommendations.add(goal['goal'])

        # Add skill profile based recommendations (top profiles)
        for profile in skill_profiles:
            recommendations.add(profile['profile'])

        # Return unique recommendations as list
        return list(recommendations)
