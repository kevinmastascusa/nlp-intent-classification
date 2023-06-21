# Example intent categories and their respective confidence scores
intent_categories = {
    "greeting": 0.9,
    "farewell": 0.8,
    "weather": 0.7
}

# Threshold for considering a query as out-of-scope
threshold = 0.6

def recognize_intent(query):
    # Perform intent recognition logic here (e.g., using a trained model)
    # For simplicity, we'll randomly assign an intent category and confidence score
    recognized_intent = random.choice(list(intent_categories.keys()))
    confidence_score = intent_categories[recognized_intent]
    
    return recognized_intent, confidence_score

def handle_query(query):
    recognized_intent, confidence_score = recognize_intent(query)
    
    if confidence_score >= threshold:
        # Query falls within a recognized intent category
        print("Intent:", recognized_intent)
        # Handle the query based on the recognized intent
        
    else:
        # Query is out-of-scope
        print("Out-of-scope query")
        # Provide an appropriate response for out-of-scope queries

# Example queries
queries = [
    "Hello, how are you?",
    "What's the weather like today?",
    "Tell me a joke!",
    "Find the nearest coffee shop."
]

# Process each query
for query in queries:
    handle_query(query)
    print("---")
