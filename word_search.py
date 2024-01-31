# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:18:38 2023

@author: dell
"""
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

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

def find_similar_words(input_word, word_vectors, top_n=3):
    if input_word in word_vectors:
        input_vector = np.array([word_vectors[input_word]])
        all_words = list(word_vectors.keys())
        all_vectors = np.array([word_vectors[word] for word in all_words])
        similarities = cosine_similarity(input_vector, all_vectors)
        most_similar_indices = np.argsort(similarities[0])[::-1][:top_n]
        most_similar_words = [all_words[idx] for idx in most_similar_indices]
        return most_similar_words
    else:
        return []
while True:
    
    input_word = input("Enter a word: ")
    
    if input_word == 'EXIT' or input_word == 'exit' :
        break
    else:
        similar_words = find_similar_words(input_word, word_vectors, top_n=3)
        print(f"Similar words to '{input_word}': {similar_words}") 

