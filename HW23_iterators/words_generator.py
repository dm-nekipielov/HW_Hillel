import random

import requests


def words_generator(num_words: int):
    word_url = "https://norvig.com/ngrams/enable1.txt"
    response_txt = requests.get(word_url).text
    words = response_txt.splitlines()
    if num_words > 10000:
        return "Should be less than 10000 words"
    for _ in range(num_words):
        yield words.pop(random.randint(0, len(words)))
