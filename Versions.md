# Version Information Tracker

## Version 0.1
Started working on the basic port scanner, it has the display banner function for aesthetics, the connection function where the socket connects with the port of the target and prints out if its opened or closed. The port_scanner function that focuses on looping the connection function for every port as an argument. Lastly main that calls the banner function and the port_scanner function.

Disadvantages:  
- Very Slow
- Checks ALL ports
- No user Input or any argument modification

Improvement for 0.2
- [ ] Add threading
- [ ] Scans port range depending on user Req
- [ ] add arguments and user input
- [ ] Adding verbose mode
