# Usesing this to avoid reusing the codes in every file
import pyfiglet
import chardet

# Displays the banner
def display_banner():
    ### Extra for banner printing
    fonts = pyfiglet.FigletFont.getFonts()
    chosen_font = "standard"  # Replace with the font of your choice
    fig = pyfiglet.Figlet(font=chosen_font)
    banner = fig.renderText("Snom")
    print(banner)
    print("Snom 0.3. A Port Scanner Project by AtomicScript")
    print("-"*50)


# returns a list of ports
def handle_port_input(port_input):
    try:
        # checks
        if ',' in port_input:
            return port_input.split(',')

        elif '-' in port_input:
            start, end = port_input.split('-')
            ports = []
            for i in range(int(start), int(end)+1):
                ports.append(i)
            return ports

    except:
        return "None"


def detected_encoding_decode(raw):
    # chardet tries to detect the encoded message
    detected_encoding = chardet.detect(raw)['encoding']
    # if detected_encoding is none then use utf-8
    if detected_encoding is None:
        detected_encoding = 'utf-8'
    # decode using the detected encoding
    decoded = raw.decode(detected_encoding).strip()
    # return
    return decoded
