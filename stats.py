def get_num_words(filepath):
    with open(filepath) as f:
        text = f.read()
        words = text.split()
        num_words = len(words)
    return num_words

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

from collections import Counter

def count_characters(filepath):
    with open(filepath) as f:
        text = f.read()
        text = text.lower()
        
        characters = Counter(text)
        



    return characters