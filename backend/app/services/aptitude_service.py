class AptitudeService:
    def predict_aptitude(self, scores: list[float]) -> int:
        # Simple average-based classification
        avg = sum(scores) / len(scores)
        if avg >= 80:
            return 3  # High aptitude
        elif avg >= 60:
            return 2  # Moderate aptitude
        else:
            return 1  # Low aptitude
