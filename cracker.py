import argparse
import os
from sys import stderr


from utils.Cracker import Cracker
from utils.Shadow import ShadowFile, AlgorithmTable 
from utils.Passwd import PasswdFile 


if __name__ == "__main__":
    # Parse Command Line arguments.
    PARSER = argparse.ArgumentParser("./backdoor.py")
    PARSER.add_argument("shadow_file", help="Path to the shadow file.")
    PARSER.add_argument("wordlist_file", help="Path to the wordlist file.")
    PARSER.add_argument("-u", "--usernames", dest="usernames", help="A comma-separated list of usernames, only the given users will be targeted.", required=False)
    ARGS = PARSER.parse_args()
    
    if not os.path.isfile(ARGS.wordlist_file):
        print(f"ERROR: File not found '{ARGS.wordlist_file}'", file=stderr)
        exit(1)

    if ARGS.usernames is None:
        userlist = []
    else:
        userlist = ARGS.usernames.split(",")

    shadow_file = ShadowFile("shadow")
    cracker = Cracker(shadow_file, userlist, ARGS.wordlist_file) 
    cracker.crack()

