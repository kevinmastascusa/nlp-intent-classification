import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim import corpora
from gensim.models import LdaModel
from pprint import pprint

# Sample corpus for topic modeling
corpus = [
    "The cat sat on the mat",
    "The dog chased the cat",
    "The mouse ran away from the cat and the dog",
    "The bird flew high in the sky",
    "The cat and the dog were friends",
    "The mouse and the bird were enemies"
]

# Tokenization and preprocessing
stop_words = set(stopwords.words("english"))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    return filtered_tokens

# Preprocessing the corpus
processed_corpus = [preprocess(doc) for doc in corpus]

# Creating a dictionary from the preprocessed corpus
dictionary = corpora.Dictionary(processed_corpus)

# Creating a bag-of-words representation of the corpus
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_corpus]

# Training the LDA model
lda_model = LdaModel(bow_corpus, num_topics=3, id2word=dictionary, passes=10)

# Printing the topics and their keywords
pprint(lda_model.print_topics())

# Inferring topics for a new document
new_doc = "The cat and the mouse played together"
new_doc_bow = dictionary.doc2bow(preprocess(new_doc))
pprint(lda_model.get_document_topics(new_doc_bow))
