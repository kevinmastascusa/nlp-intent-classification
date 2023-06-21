from gensim import corpora, models

def perform_topic_modeling(documents):
    # Prepare the documents for topic modeling
    texts = [[token for token in document.lower().split()] for document in documents]

    # Create a dictionary and convert the documents into a bag-of-words corpus
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]

    # Perform topic modeling using LDA
    lda_model = models.LdaModel(corpus, num_topics=5, id2word=dictionary)

    # Print the topics
    for idx, topic in lda_model.print_topics():
        print(f"Topic {idx+1}: {topic}")
    
    return lda_model

# User interface loop
documents = []
print("Enter pathology report text (type 'done' when finished):")
while True:
    user_input = input()
    if user_input.lower() == "done":
        break
    documents.append(user_input)

lda_model = perform_topic_modeling(documents)
print()
