# Version Information Tracker

## Versions:

### Version 0.3
In this iteration:

- Implemented the port range functionality in `functions.py` to intelligently handle port inputs, discerning between comma-separated lists and ranges. The resultant function returns a list of ports.
- Transitioned from employing `optparse` to utilizing `argparse` for command-line argument parsing. This change enhances code comprehensibility and maintainability.
- Introduced the `detected_encoding_decode` feature to decode responses from the target.
Enacted a banner grabbing mechanism; however, it's important to note that this feature may not yield results for all ports or services.

### Version 0.2
This version encompassed several notable enhancements:

- Created a dedicated Functions file to house repetitive code segments, such as the display banner function.
- Renamed the port scanner function to "scanner handler" to better encapsulate its role in managing different ports.
- Rebranded the connection function as "port_scanner," reflecting its function as the point of initiation and testing for connections.

Notable Updates:

- Refactored the "display banner" `function` to be referred to as "Snom."
- Incorporated the usage of `optparse` to facilitate user input of target and port specifications.
- Added a predefined set of "common ports" for cases where users do not provide specific port ranges.
- Introduced multi-threading capabilities with a maximum of 300 threads.
- Integrated a "verbose" mode (-v) for more extensive output.

Considerations:
Consider revising the utilization of `connect_ex`to `connect` for improved efficiency. Further investigation is required to ascertain version information or other pertinent details in cases of successful connections. In instances of failed connections, it is advisable to conduct additional checks to confirm whether the port is genuinely closed or merely filtered, albeit at the potential cost of reduced scan speed.

### Version 0.1
This initial version focused on establishing the foundational elements of the port scanner:

- Included the "display banner" function for aesthetic purposes.
- Introduced the "connection" function, responsible for establishing socket connections with the target ports and displaying whether they are open or closed.
- Implemented the "port_scanner" function, designed to iterate through the various ports specified as arguments.
- Concluded with the "main" function, which calls both the banner and port_scanner functions.

Limitations:
- Demonstrated relatively slow performance.
- Scanned all available ports.
- Lacked user input capabilities and argument modifications.

Anticipated Improvements for Version 0.2
