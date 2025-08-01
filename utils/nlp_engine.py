import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

def match_skills(text):
    tokens = word_tokenize(text)
    keywords = ['sales', 'python', 'driver', 'plumber', 'electrician']
    return [kw for kw in keywords if kw in tokens]
