When running from packages_resolution, run consumer.py like this:
python3 -m client.consumer

This tells python we are running a module and not a file.

# Python packages / Directory resolution

1. When you run a python file using python abc.py, it only puts the folder where the python file resides, into the current working directory (sys.path)

2. For example if I have calc.py and then client --> consumer.py. Then if I run consumer.py, it won't work because python won't be able to import calc.py.

3. Now, we can run it as python3 -m client.consumer, this will treat the client.consumer as a module. This means that it tells python to start with the current directory (from where we are running) as the root package, and then go to client and then to consumer. This tells python: "Don't run this as a random file. Treat it as part of a package hierarchy".