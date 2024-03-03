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


def ask(prompt: str, valid: list[str] = None) -> str:
    try_word = input(prompt)
    while valid and try_word not in valid:
        try_word = input(prompt)
    return try_word


parser = argparse.ArgumentParser()
parser.add_argument("words", default='https://gitlab.com/zenoro/coop-py-dev2023/03_MergeRequirements/defaultdict.txt', type=str)
parser.add_argument("length", nargs="?", default=5, type=int)
args = parser.parse_args()

if args.words.startswith("https://") or args.words.startswith("http://") or args.words.startswith("ftp://"):
    file = urllib.request.urlretrieve(args.words)[0]
    with open(file, "r") as fd:
        dictwords = [line.strip() for line in fd if line and len(line.strip()) == args.length]
else:
    bufmsg = args.words
    for _ in range(2):
        try:
            with open(bufmsg, "r") as fd:
                dictwords = [line.strip() for line in fd if line and len(line.strip()) == args.length]
            break
        except FileNotFoundError:
            bufmsg = getcwd() + bufmsg.strip()
            continue
    else:
        quit("Неверный путь к словарю слов. Попробуйте указать URL-адрес или локальный файл")

print(gameplay(ask, inform, dictwords))
