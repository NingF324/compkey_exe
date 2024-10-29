def word_similarity(word1, word2):
    similarity = 0
    if word1 in word2 or word2 in word1:
        similarity = 0.95
    return similarity >= 0.9
