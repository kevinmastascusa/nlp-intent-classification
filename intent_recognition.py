import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC

# Sample labeled dataset for intent recognition
training_data = [
    ("Hi there", "greeting"),
    ("Hello", "greeting"),
    ("Goodbye", "farewell"),
    ("Bye", "farewell"),
    ("See you later", "farewell"),
]

# Tokenization and preprocessing
stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    return " ".join(filtered_tokens)

# Preprocessing training data
corpus = [preprocess(text) for text, intent in training_data]
labels = [intent for text, intent in training_data]

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)

# Training the intent classifier
classifier = SVC(kernel="linear")
classifier.fit(X, labels)

# Intent recognition function
def recognize_intent(user_input):
    preprocessed_input = preprocess(user_input)
    input_vector = vectorizer.transform([preprocessed_input])
    predicted_intent = classifier.predict(input_vector)[0]
    return predicted_intent

# Interactive chatbot loop
while True:
    user_input = input("User: ")
    intent = recognize_intent(user_input)
    
    if intent == "greeting":
        print("Bot: Hello! How can I assist you?")
    elif intent == "farewell":
        print("Bot: Goodbye! Have a nice day!")
    else:
        print("Bot: Sorry, I didn't understand. Could you please rephrase?")
