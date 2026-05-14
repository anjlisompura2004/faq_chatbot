import nltk
nltk.download('punkit')
nltk.download('punkt_tab')
import numpy as np
import random
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download punkt tokenizer
nltk.download('punkt')

# Read FAQ file
with open('faqs.txt', 'r') as file:
    data = file.read().lower()

# Split into question-answer pairs
faq_pairs = [line.split('|') for line in data.split('\n') if '|' in line]

questions = [pair[0] for pair in faq_pairs]
answers = [pair[1] for pair in faq_pairs]

# Text preprocessing
def preprocess(text):
    tokens = nltk.word_tokenize(text)
    tokens = [word for word in tokens if word not in string.punctuation]
    return ' '.join(tokens)

# Chatbot response function
def get_response(user_input):
    user_input = preprocess(user_input.lower())

    all_questions = questions + [user_input]

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(all_questions)

    similarity = cosine_similarity(tfidf[-1], tfidf[:-1])

    index = similarity.argmax()
    score = similarity[0][index]

    if score < 0.2:
        return "Sorry, I don't understand your question."
    else:
        return answers[index]

# Chat loop
print("FAQ Chatbot (type 'exit' to stop)")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break

    response = get_response(user_input)
    print("Bot:", response)