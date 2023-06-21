from transformers import pipeline

# Load the pre-trained text summarization model
model = "t5-base"
summarizer = pipeline("summarization", model=model, tokenizer=model)

# User interface loop
while True:
    user_input = input("Enter clinical text to summarize (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    summary = summarizer(user_input, max_length=100, min_length=30, do_sample=True)[0]["summary_text"]
    print("Summary:", summary)
    print()
