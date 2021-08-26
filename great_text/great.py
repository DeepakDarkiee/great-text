from pyfiglet import Figlet
from termcolor import colored


def great_text(text: str = "Hello", color: str = "red", font: str = "None"):
    if font == "None":
        print(colored(text, color))
    else:
        f = Figlet(font=font)
        print(colored(f.renderText(text), color))


if __name__ == "__main__":
    great_text("Hello", "red", "isometric2")
