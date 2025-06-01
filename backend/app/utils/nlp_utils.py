import re

def clean_text(text: str) -> str:
    # Basic preprocessing
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text.strip()

def extract_keywords(text: str, keyword_list: list[str]) -> list[str]:
    found = []
    for kw in keyword_list:
        if kw.lower() in text:
            found.append(kw)
    return found
