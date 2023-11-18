from colorama import Fore, Back, Style


class Errorama:
    def __init__(self) -> None:
        pass

    def panic(msg: str) -> None:
        raise Exception(Fore.RED + f"❌: {msg}")

    def warn(warn: str) -> None:
        print(Fore.YELLOW + f"⚠️: {warn}")
        print(Style.RESET_ALL)

    def success(sen: str) -> None:
        print(Fore.GREEN + "✔️:" + sen)
        print(Style.RESET_ALL)
