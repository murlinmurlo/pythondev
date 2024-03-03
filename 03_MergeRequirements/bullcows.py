import random
import urllib.request
import argparse


def bullscows(guess: str, secret: str) -> (int, int):
    bulls, cows = 0, 0
    for i, j in enumerate(guess):
        if j == secret[i]:
            bulls += 1
        elif j in secret:
            cows += 1
    return (bulls, cows)

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    attempt = 1
    word = random.choice(words)
    try_word = ask("Введите слово: ", words)
    while try_word != word:
        bulls, cows = bullscows(try_word, word)
        inform("Быки: {}, Коровы: {}", bulls, cows)
        attempt += 1
        try_word = ask("Введите слово: ", words)
    if try_word.lower() == word.lower():
        return attempt

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))