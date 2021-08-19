from pyfiglet import Figlet
from termcolor import colored


def great_text(text: str, font: str, color: str):
    f = Figlet(font=font)
    print(colored(f.renderText(text), color))


if __name__ == "__main__":
    great_text("Hello", "isometric2", "red")
