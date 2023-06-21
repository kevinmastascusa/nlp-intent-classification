from transformers import pipeline

# Load the pre-trained question-answering model
model = "distilbert-base-cased-distilled-squad"
qa_pipeline = pipeline("question-answering", model=model)

# User interface loop
while True:
    context = input("Enter the context: ")
    if context.lower() == "exit":
        break
    question = input("Enter the question: ")

    # Perform question-answering
    result = qa_pipeline(question=question, context=context)

    # Extract the answer
    answer = result["answer"]
    confidence = result["score"]

    # Display the answer and confidence score
    print("Answer:", answer)
    print("Confidence Score:", confidence)
    print()
