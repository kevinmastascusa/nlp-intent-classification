import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

# Sample text for named entity recognition
text = "Apple Inc. was founded in 1976 by Steve Jobs, Steve Wozniak, and Ronald Wayne. It is headquartered in Cupertino, California."

# Tokenization and part-of-speech tagging
tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)

# Named entity recognition
ner_tags = ne_chunk(pos_tags)

# Extracting named entities
named_entities = []
for entity in ner_tags.subtrees():
    if entity.label() != 'S':
        named_entities.append(' '.join([word for word, _ in entity.leaves()]))

# Printing the named entities
for entity in named_entities:
    print(entity)
