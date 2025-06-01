# app/models/goal_extractor.py

from transformers import pipeline

class GoalExtractor:
    def __init__(self):
        # Using a HuggingFace zero-shot classification pipeline for demo
        self.classifier = pipeline("zero-shot-classification",
                                   model="facebook/bart-large-mnli")

        self.candidate_labels = [
            "engineering", "medical", "law", "arts", "commerce",
            "civil services", "accounting", "teaching", "research"
        ]

    def extract_goals(self, text):
        result = self.classifier(text, self.candidate_labels)
        # Return top 2 goals by score
        goals = []
        for label, score in zip(result['labels'], result['scores']):
            if score > 0.2:  # threshold
                goals.append({"goal": label, "confidence": float(score)})
        return goals[:2]
