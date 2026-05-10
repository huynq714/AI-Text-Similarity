import re
from underthesea import word_tokenize

STOPWORDS = {
    "và", "là", "của", "có", "được",
    "những", "các", "một", "trong"
}

def preprocess_text(text):
    text = text.lower()

    text = re.sub(r'[^\w\s]', '', text)

    words = word_tokenize(text)

    words = [w for w in words if w not in STOPWORDS]

    return " ".join(words)