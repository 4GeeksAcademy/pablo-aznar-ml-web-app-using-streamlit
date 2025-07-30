import re
from nltk import download
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

download("wordnet")
download("stopwords")

lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words("english")

def preprocess_text(text):
    text = text.lower()
    # Reemplazar extensiones por espacios
    text = re.sub(r'https?://|www\.|\.com|\.html|\.pdf|\.gov|\.net|\.org|\.edu|\.php|\.aspx', ' ', text)

    # Eliminar cualquier caracter que no sea una letra (a-z) o un espacio en blanco ( )
    text = re.sub(r'[^a-z ]', " ", text)

    # Eliminar espacios en blanco
    text = re.sub(r'\s+[a-zA-Z]\s+', " ", text)
    text = re.sub(r'\^[a-zA-Z]\s+', " ", text)

    # Reducir espacios en blanco múltiples a uno único
    text = re.sub(r'\s+', " ", text)

    return text.split()

def lemmatize_text(words, lemmatizer = lemmatizer):
    tokens = [lemmatizer.lemmatize(word) for word in words]
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [word for word in tokens if len(word) > 3]
    return tokens