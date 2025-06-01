class SkillGapService:
    def analyze_gap(self, career_path: str, user_skills: list[str]) -> list[str]:
        required_skills_map = {
            "Data Scientist": ["python", "statistics", "machine learning"],
            "Doctor": ["biology", "anatomy", "medical knowledge"],
            "IAS Officer": ["current affairs", "essay writing", "reasoning"],
        }
        required = required_skills_map.get(career_path, [])
        missing = [skill for skill in required if skill not in user_skills]
        return missing
