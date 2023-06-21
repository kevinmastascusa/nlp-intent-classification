from collections import defaultdict
import random

def train_ngram_model(corpus, n):
    ngram_counts = defaultdict(int)
    context_counts = defaultdict(int)
    
    # Count n-gram occurrences and context occurrences
    for sentence in corpus:
        tokens = sentence.split()
        for i in range(len(tokens)-n+1):
            ngram = tuple(tokens[i:i+n])
            context = tuple(tokens[i:i+n-1])
            ngram_counts[ngram] += 1
            context_counts[context] += 1
    
    # Calculate probabilities based on counts
    ngram_probabilities = defaultdict(float)
    for ngram, count in ngram_counts.items():
        context = ngram[:-1]
        context_count = context_counts[context]
        probability = count / context_count
        ngram_probabilities[ngram] = probability
    
    return ngram_probabilities

def generate_text(ngram_probabilities, n, length):
    generated_text = []
    context = ('<start>',) * (n-1)
    
    for _ in range(length):
        next_word = random.choices(list(ngram_probabilities.keys()), list(ngram_probabilities.values()), k=1)[0][-1]
        generated_text.append(next_word)
        context = context[1:] + (next_word,)
    
    return ' '.join(generated_text)

# Example usage
corpus = [
    "I like to eat pizza",
    "Pizza is delicious",
    "I enjoy eating burgers"
]

n = 2  # Change this to the desired n-gram value
length = 10  # Change this to the desired length of the generated text

ngram_probabilities = train_ngram_model(corpus, n)
generated_text = generate_text(ngram_probabilities, n, length)

print("Generated Text:", generated_text)
