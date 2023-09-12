import socket
import pyfiglet

# Displays the banner
def display_banner():
    ### Extra for banner printing
    fonts = pyfiglet.FigletFont.getFonts()
    chosen_font = "standard"  # Replace with the font of your choice
    fig = pyfiglet.Figlet(font=chosen_font)
    banner = fig.renderText("Scanner v0.1")
    print(banner)

# focus on connecing with the port
def connection(target, port):
    try:
        # creating a low level socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            # returns:
            # 0 = connection successful
            # 111 = connection refused
            # 61 = connection refused
            # 110 = timeout  (firewall or port closed)
            ex = s.connect_ex((target, port))
            if ex == 0:
                print(f"[+] {port}/tcp Opened")
            else:
                print(f"[+] {port}/tcp Closed")

    except Exception as e:
        print(f"[!] Error: {e}")

# focuses on running the function connection with all ports
def port_scanner(target):
    # attempts to connect with each port range
    for port in range(1,65536):
        # slow and not needed to check all ports
        connection(target, port)

def main():
    display_banner()
    port_scanner("192.168.199.130")


if __name__ == '__main__':
    main()
