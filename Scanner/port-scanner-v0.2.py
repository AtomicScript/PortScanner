# Adding Threading, and OptParse
import optparse
import threading
import socket
from Functions import display_banner

threads = []
verbose = False
# this helps in locking the screen to print
screenLock = threading.Semaphore(value=1)

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
def scanner_handler(target, ports):
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


# Creating the optparse class in main to recieve the user input
def main():
    global verbose
    ### OPT OptParse
    # optparse object
    parser = optparse.OptionParser()
    ## adding options like target and port
    parser.add_option("-t", dest="tgtHost", type="string", help="Specify the target ip address")
    parser.add_option("-p", dest="tgtPort", type="string", help="Specify the target property")
    parser.add_option("-v", dest="verbose", default=False, action="store_true", help="verbose")

    # getting the options and the arguments for the options
    options, args = parser.parse_args()
    tgtHost = options.tgtHost
    # adding the split "," to accept more than one making this a list
    tgtPorts = str(options.tgtPort).split(',')
    # Change the global varbale to true if verbose was activated
    verbose = options.verbose

    display_banner()
    print("[*] Port Scanner Snom has started...")
    print(f"[*] Scanning target : {tgtHost}")


    if tgtPorts[0] == "None":
        # If no ports are used we will be activating the common ports
        tgtPorts = [20,21,22,23,25,53,80,110,143,443,465,587,993,995,3306,3389,5432,5900,8080]
        print(f"[*] Activated scanning for the common port numbers")

    if verbose:
        print("[*] Verbose mode was activated")

    print("-"*50)
    scanner_handler(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()
