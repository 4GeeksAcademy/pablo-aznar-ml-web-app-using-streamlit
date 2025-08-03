import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Comprueba y descarga recursos solo si faltan
try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words("english")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'https?://|www\.|\.com|\.html|\.pdf|\.gov|\.net|\.org|\.edu|\.php|\.aspx', ' ', text)
    text = re.sub(r'[^a-z ]', " ", text)
    text = re.sub(r'\s+[a-zA-Z]\s+', " ", text)
    text = re.sub(r'\^[a-zA-Z]\s+', " ", text)
    text = re.sub(r'\s+', " ", text)
    return text.split()

def lemmatize_text(words, lemmatizer=lemmatizer):
    tokens = [lemmatizer.lemmatize(word) for word in words]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [word for word in tokens if len(word) > 3]
    return tokens