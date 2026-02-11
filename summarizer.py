import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import defaultdict

nltk.download('punkt')
nltk.download('stopwords')

def summarize_text(text, lines=3):
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())

    stop_words = set(stopwords.words('english'))
    word_freq = defaultdict(int)

    for word in words:
        if word.isalnum() and word not in stop_words:
            word_freq[word] += 1

    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] += word_freq[word]

    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    return " ".join(summary[:lines])


text = """
Artificial Intelligence is transforming industries worldwide.
It allows machines to learn from data and make decisions.
AI is used in healthcare, education, and finance.
Ethical concerns and data privacy remain challenges.
"""

print("SUMMARY:\n")
print(summarize_text(text))
