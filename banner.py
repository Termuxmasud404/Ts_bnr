import os
import random

COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}

RESET = "\033[0m"

def color_banner(text, color):
    return f"{COLORS[color]}{text}{RESET}"

def main():
    os.system("clear")

    banner_text = "Termux Banner Script"
    colors = list(COLORS.keys())
    random.shuffle(colors)

    for color in colors:
        print(color_banner(banner_text, color))

if __name__ == "__main__":
    main()
