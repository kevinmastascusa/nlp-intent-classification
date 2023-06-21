import spacy

# Load the pre-trained NER model
nlp = spacy.load("en_core_web_sm")

def recognize_entities(text):
    # Perform named entity recognition using SpaCy
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

# User interface loop
while True:
    user_input = input("Enter pathology report text (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    entities = recognize_entities(user_input)
    print("Named Entities:")
    for entity, label in entities:
        print(f"{entity} - {label}")
    print()
