# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 21:42:12 2023

@author: dell
"""

import numpy as np
from sklearn.metrics.pairwise import euclidean_distances


def load_word_vectors(file_path):
    word_vectors = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            word = parts[0]
            vector = [float(x) for x in parts[1:]]
            word_vectors[word] = vector
    return word_vectors

word_vectors = load_word_vectors('word_embeddings.txt')

def find_analogy(word1, word2, word3, word_vectors, top_n=2):
    
    word1 = word1.lower()
    word2 = word2.lower()
    word3 = word3.lower()
    
    if word1 in word_vectors and word2 in word_vectors and word3 in word_vectors:
        vec1 = np.array(word_vectors[word1])
        vec2 = np.array(word_vectors[word2])
        vec3 = np.array(word_vectors[word3])
        
        analogy_vector = vec3 + (vec2 - vec1)
        all_words = list(word_vectors.keys())
        all_vectors = np.array([word_vectors[word] for word in all_words])
        distances = euclidean_distances([analogy_vector], all_vectors)
        
        nearest_indices = np.argsort(distances[0])[:top_n]
        nearest_words = [all_words[idx] for idx in nearest_indices]        
        return nearest_words
    else:
        return []
    
analogies = [
    ('king', 'queen', 'prince'),
    ('finland', 'helsinki', 'china'),
    ('love', 'kiss', 'hate')
]

for analogy in analogies:
    word1, word2, word3 = analogy
    results = find_analogy(word1, word2, word3, word_vectors, top_n=2)
    print(f"{word1} is to {word2} as {word3} is to:")
    for i, word in enumerate(results):
        print(f"Top {i+1}: {word}")
    print()
