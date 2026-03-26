# EndPoint
This is tool that allows for fetching information about a minecraft java server with just a server ip address.

# Quick Disclaimer
This tool does not assist in finding IP Adresses to minecraft servers and only allows viewing of data from servers
which IPs you already know.

# Installation
Option 1:
Just go to the releases tab and find the latest release. Once there you can either grab
the CLI version or the GUI version and run it with

```python3 EndPoint_VerX.py``` or ```python3 EndPoint_VerXCLI.py```

Option 2:
If you do not wish to use the python script in the latest version you can run
```
    git clone https://github.com/Proxieru/EndPoint.git
    cd EndPoint
    pip install -r requirements.txt
    python3 EndPoint_VerX.py
```
# Features
- MOTD
  EndPoint will give you the MOTD of the server once a ip is submitted. It also formats it to be readable. (I will eventully add a way to view raw   MOTD)
  it will also color it. (Broke somehow, I will fix it eventully)

- Version
  Self explanitory, It will display the version(s) the server reported and the protocol version.

- Error reporting
  It will tell you the errors under the Input Server portion once they occur.

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
