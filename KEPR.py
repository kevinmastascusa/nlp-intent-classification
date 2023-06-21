import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def extract_keywords(text):
    # Tokenize the text and remove stop words
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(text)
    keywords = [token for token in tokens if token.lower() not in stop_words]

    return keywords

# User interface loop
while True:
    user_input = input("Enter pathology report text (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    keywords = extract_keywords(user_input)
    print("Keywords:", keywords)
    print()
