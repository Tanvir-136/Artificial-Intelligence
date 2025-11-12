def generate_ngrams(text, n):
    # Step 1: split the sentence into words
    words = text.split()

    # Step 2: create n-grams
    ngrams = []
    for i in range(len(words) - n + 1):
        ngram = ' '.join(words[i:i+n])
        ngrams.append(ngram)
    
    return ngrams

# Example usage
sentence = "I love learning about artificial intelligence"

# Also print unigram, bigram, and trigram separately
print("Unigram:", generate_ngrams(sentence, 1))
print("Bigram:", generate_ngrams(sentence, 2))
print("Trigram:", generate_ngrams(sentence, 3))