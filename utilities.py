import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


def lowercase_folding(text):
    return text.lower()


def normalize(text):
    return {word.translate(str.maketrans('', '', string.punctuation)).lower() for word in text}


def remove_stopwords(text):
    stop_words = set(stopwords.words('english')) | set(
        stopwords.words('french'))
    return set([w.lower() for w in text if not w in stop_words])


def stem(text):
    stemmer = PorterStemmer()
    return set([stemmer.stem(w).lower() for w in text])