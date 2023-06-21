import torch
from transformers import MarianMTModel, MarianTokenizer

def translate_text(text, source_lang, target_lang):
    # Load the pre-trained machine translation model and tokenizer
    model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Tokenize the input text
    inputs = tokenizer.prepare_translation_batch(src_texts=[text])

    # Translate the text
    translated = model.generate(**inputs)

    # Decode the translated text
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)

    return translated_text

# User interface
source_language = input("Enter the source language: ")
target_language = input("Enter the target language: ")
text = input("Enter the text to translate: ")

translated_text = translate_text(text, source_language, target_language)
print("Translated Text:", translated_text)
