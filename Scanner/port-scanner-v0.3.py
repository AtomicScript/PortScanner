# Adding Threading, and OptParse
import optparse, argparse
import threading
import socket
from Functions import *

threads = []
verbose = False
opened_ports = []
# this helps in locking the screen to print
screenLock = threading.Semaphore(value=1)

def banner_scanner(target, port):
    try:
        # create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((target, port))
        # for decoding, different data uses different endocing
        raw_banner = s.recv(1024)
        banner = detected_encoding_decode(raw_banner)
        s.close()
        screenLock.acquire()
        print(f"[+] Port {port}: {banner}")
        screenLock.release()

    except Exception as err:
        s.close()
        screenLock.acquire()
        print(f"[!] Error {err}")
        # release the lock to continue
        screenLock.release()


# this function focuses on connecting with the each port
def port_scanner(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # port should be an int
            s.settimeout(5)
            ex = s.connect_ex((target, int(port)))
            if ex == 0:
                screenLock.acquire()
                print(f"[+] Port {port}/tcp Opened")
                opened_ports.append(port)
            # only if verbose
            elif ex != 0 and verbose == True:
                screenLock.acquire()
                print(f"[-] Port {port}/tcp Closed")

            s.close()
    except Exception as err:
        screenLock.acquire()
        print(f"[!] Error {err}")
        s.close()
    # release the lock to continue
    screenLock.release()

# Port scanner_handler function just helps with the looping
def port_scanner_handler(target, ports):
    ## Adding threading but need to limit it to 300 to avoid erros
    for port in ports:
        # checks if we have the limited number of active threads
        while threading.active_count()>=300:
            pass
        # create the thread
        t = threading.Thread(target=port_scanner,args=(target,int(port)))
        # adds it to the thread list
        threads.append(t)
        # start the thread
        t.start()

    for t in threads:
        t.join()

def port_services_handler(target):
    ## Adding threading but need to limit it to 300 to avoid erros
    for port in opened_ports:
        # checks if we have the limited number of active threads
        while threading.active_count()>=300:
            pass
        # create the thread
        t = threading.Thread(target=banner_scanner,args=(target,int(port)))
        # adds it to the thread list
        threads.append(t)
        # start the thread
        t.start()

    for t in threads:
        t.join()

# Creating the optparse class in main to recieve the user input
def main():
    global verbose
    # creating the argument parser object with description
    parser = argparse.ArgumentParser(description='Snom 0.3 Port scanner created by AtomicScript')

    # adding argparse option
    parser.add_argument('-t', '--target', dest='tgtHost', help='Specify the target ip address')
    parser.add_argument('-p', '--port', dest='tgtPort', help='Specify the ports to be scanned')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')

    # getting the options and the arguments for the options
    args = parser.parse_args()
    tgtHost = args.tgtHost
    # handles the port input
    tgtPorts = handle_port_input(args.tgtPort)
    # Change the global varbale to true if verbose was activated
    verbose = args.verbose

    if  tgtHost == "None" or tgtHost == None:
        parser.print_help()
        exit()

    display_banner()
    print(f"[*] Scanning target : {tgtHost}")

    if tgtPorts == "None" or tgtPorts[0] == "None":
        print(f"[*] Activated scanning for the common port numbers")
        tgtPorts = [20,21,22,23,25,53,80,110,143,443,465,587,993,995,3306,3389,5432,5900,8080]
        # If no ports are used we will be activating the common ports


    if verbose:
        print("[*] Verbose mode was activated")

    print("-"*50)
    print("[*] Port Scanner has started")
    port_scanner_handler(tgtHost, tgtPorts)
    print("-"*50)
    print("[*] Port Banner Grabbing has started")
    port_services_handler(tgtHost)


if __name__ == '__main__':
    main()
