from errorHandler import Errorama
import wikipedia
import os
from colorama import Fore, Back, Style

errh = Errorama()


def summary(subj, path) -> None:
    with open(path, "a") as f:
        sum = wikipedia.summary(subj, sentences=2)
        print(sum)
        ppath = os.path.abspath(path)
        op = f" saved at :"
        print(Fore.GREEN + f"saved at {path}")

        f.write(sum)
