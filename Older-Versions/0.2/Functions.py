# Usesing this to avoid reusing the codes in every file
import pyfiglet

# Displays the banner
def display_banner():
    ### Extra for banner printing
    fonts = pyfiglet.FigletFont.getFonts()
    chosen_font = "standard"  # Replace with the font of your choice
    fig = pyfiglet.Figlet(font=chosen_font)
    banner = fig.renderText("Snom")
    print(banner)
    print("Current version: 0.2")
    print("A project by AtomicScript")
    print("-"*50)
