import os

def clear_screen():
    os.system('clear')

def print_banner(text):
    os.system('echo "\033[1;31m' + text + '\033[0m"')

def main():
    clear_screen()
    print_banner('TERMUX BANNER')

if __name__ == '__main__':
    main()
