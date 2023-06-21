import os
import re
from collections import defaultdict
from nltk.tokenize import word_tokenize

def build_index(directory):
    index = defaultdict(list)
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            text = file.read()
            tokens = word_tokenize(text)
            for token in tokens:
                # Remove special characters and convert to lowercase
                cleaned_token = re.sub(r'[^a-zA-Z0-9]', '', token.lower())
                index[cleaned_token].append(filename)
    return index

# User interface
directory_path = input("Enter the path to the directory containing web pages: ")
search_term = input("Enter a search term: ")
index = build_index(directory_path)
results = index.get(search_term.lower(), [])
print("Search Results:")
if results:
    for filename in results:
        print(filename)
else:
    print("No results found.")
