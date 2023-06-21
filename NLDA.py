import nltk
from nltk.tokenize import sent_tokenize

def diagnose(text):
    # Perform diagnosis using NLP techniques
    # Add your diagnostic logic here
    diagnosis = "Example diagnosis"
    return diagnosis

# User interface loop
while True:
    user_input = input("Enter patient symptoms or medical records (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    sentences = sent_tokenize(user_input)
    diagnosis = diagnose(sentences)
    print("Diagnosis:", diagnosis)
    print()
