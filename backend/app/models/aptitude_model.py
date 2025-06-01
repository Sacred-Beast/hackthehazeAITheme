# app/models/aptitude_model.py

import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

class AptitudeModel:
    def __init__(self):
        self.model_path = os.path.join(os.path.dirname(__file__), "aptitude_model.joblib")
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
        else:
            self.model = self._train_dummy_model()
            joblib.dump(self.model, self.model_path)

    def _train_dummy_model(self):
        # Dummy data: features are test scores in 3 subjects, label is aptitude class (0-3)
        X = np.array([
            [80, 75, 90],
            [50, 60, 55],
            [90, 95, 93],
            [30, 40, 35],
            [85, 80, 88],
            [45, 50, 42],
            [78, 85, 80],
            [20, 25, 30],
        ])
        y = np.array([3, 1, 3, 0, 3, 1, 2, 0])  # 0=low, 1=medium, 2=high, 3=very high aptitude
        clf = RandomForestClassifier(n_estimators=10, random_state=42)
        clf.fit(X, y)
        return clf

    def predict(self, scores):
        # scores is a list or array: [score1, score2, score3]
        scores = np.array(scores).reshape(1, -1)
        pred_class = self.model.predict(scores)[0]
        return pred_class
