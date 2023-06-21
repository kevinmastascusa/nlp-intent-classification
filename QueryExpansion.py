import gensim.downloader as api
from nltk.corpus import wordnet

def expand_query(query, top_n=5):
    model = api.load('glove-wiki-gigaword-100')
    expanded_query = []
    for word in query.split():
        synonyms = wordnet.synsets(word)
        if not synonyms:
            expanded_query.append(word)
        else:
            similar_words = model.most_similar(word, topn=top_n)
            expanded_words = [synset.lemmas()[0].name() for synset in synonyms]
            expanded_words.extend([similar_word[0] for similar_word in similar_words])
            expanded_query.extend(expanded_words)
    return ' '.join(expanded_query)

# User interface
user_query = input("Enter your search query: ")
expanded_query = expand_query(user_query)
print("Expanded Query:", expanded_query)
