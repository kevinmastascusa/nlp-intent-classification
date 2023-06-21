from transformers import MarianMTModel, MarianTokenizer

# Initialize the translation model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-fr"  # English to French translation model
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Function to perform translation
def translate(text):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    translated = model.generate(input_ids)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

# User interface loop
while True:
    user_input = input("Enter the text to translate (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    translation = translate(user_input)
    print("Translation:", translation)
