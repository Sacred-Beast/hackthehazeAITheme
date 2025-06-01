class RecommendationService:
    def recommend_careers(self, aptitude_class: int) -> list[str]:
        if aptitude_class == 3:
            return ["Data Scientist", "Doctor", "IAS Officer"]
        elif aptitude_class == 2:
            return ["Banker", "Engineer", "Marketing Manager"]
        else:
            return ["Teacher", "Sales Executive", "Technician"]
