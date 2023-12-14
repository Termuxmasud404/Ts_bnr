import pyfiglet

def create_termux_logo_banner():
    # Set the text and the font
    text = "TERMUX M45UD R4N4"
    font = "block"

    # Create the banner using pyfiglet
    banner = pyfiglet.figlet_format(text, font=font)

    # Print the banner
    print(banner)

if __name__ == "__main__":
    create_termux_logo_banner()
