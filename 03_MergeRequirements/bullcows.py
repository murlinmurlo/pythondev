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



