class SkillService:
    def map_skills(self, user_skills: list[str]) -> list[str]:
        # Placeholder matching using basic skill-to-career mapping
        mapping = {
            "python": ["Data Scientist", "Software Engineer"],
            "communication": ["Public Relations", "HR Manager"],
            "biology": ["Doctor", "Researcher"],
            "math": ["Data Analyst", "Actuary"]
        }
        recommended = set()
        for skill in user_skills:
            matches = mapping.get(skill.lower(), [])
            recommended.update(matches)
        return list(recommended)
