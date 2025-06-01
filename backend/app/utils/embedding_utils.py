from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def cosine_sim(vec1: list[float], vec2: list[float]) -> float:
    return cosine_similarity([vec1], [vec2])[0][0]

def dummy_embed(skill: str) -> list[float]:
    # Dummy 3D embedding (normally you'd use real embeddings from a model)
    return [ord(c) % 5 for c in skill.lower()[:3]]
