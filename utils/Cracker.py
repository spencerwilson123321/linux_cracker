from os import geteuid
from sys import stderr

if geteuid() != 0:
    print("ERROR: Password cracker requires root privileges!", file=stderr)
    exit(1)

class Cracker:

    def __init__(self):
        pass

