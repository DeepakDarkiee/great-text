from pyfiglet import Figlet
from termcolor import colored


def great_text(text: str = "Hello", font: str = "isometric2", color: str = "red"):
    f = Figlet(font=font)
    print(colored(f.renderText(text), color))


if __name__ == "__main__":
    great_text("Hello", "isometric2", "red")
