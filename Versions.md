# Version Information Tracker

## Versions:

### Version 0.2
I made the decision to have a file called Functions to add the repetitive codes that will rarely be updated like display banner. I renamed the port scanner function to the scanner handler since it will be handling the different ports. I also reminder the connection function to be port_scanner since it will be functions where the connection will be initiated and tested.

Updates:
- Updated the **display banner** function to be called Snom
- Added the **optparse** to take in the user target and ports
- Added **common ports** in case the user did not input any ports
- Added **threading** with max of 300 threads.
- Added **verbose** mode (-v)

Thoughts:
remove the connect_ex and change it to connect, if connect then further investigate to find version number or whatever, and else the port is closed but investigate to make sure its not filtered. This will slow down but efficient


### Version 0.1
Started working on the basic port scanner, it has the display banner function for aesthetics, the connection function where the socket connects with the port of the target and prints out if its opened or closed. The port_scanner function that focuses on looping the connection function for every port as an argument. Lastly main that calls the banner function and the port_scanner function.

Disadvantages:  
- Very Slow
- Checks ALL ports
- No user Input or any argument modification

Improvement for 0.2
