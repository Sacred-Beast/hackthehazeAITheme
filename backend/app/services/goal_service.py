class GoalService:
    def extract_goals(self, text: str) -> list[str]:
        # Placeholder goal extraction (can be enhanced using NLP models)
        keywords = ["doctor", "engineer", "IAS", "artist", "scientist", "developer", "teacher"]
        return [kw for kw in keywords if kw in text.lower()]
