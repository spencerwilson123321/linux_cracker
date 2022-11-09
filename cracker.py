import argparse
import os
from sys import stderr

from utils.Cracker import Cracker
from utils.Shadow import ShadowFile


if __name__ == "__main__":
    # Parse Command Line arguments.
    PARSER = argparse.ArgumentParser("./cracker.py")
    PARSER.add_argument("shadow_file", help="Path to the shadow file.")
    PARSER.add_argument("wordlist_file", help="Path to the wordlist file.")
    PARSER.add_argument("-u", "--users", dest="users", help="A comma-separated list of usernames, only the given users will be targeted.", required=False)
    ARGS = PARSER.parse_args()
    
    if not os.path.isfile(ARGS.wordlist_file):
        print(f"ERROR: File not found '{ARGS.wordlist_file}'", file=stderr)
        exit(1)

    if not os.path.isfile(ARGS.shadow_file):
        print(f"ERROR: File not found '{ARGS.shadow_file}'", file=stderr)
        exit(1)

    if ARGS.users is None:
        userlist = []
    else:
        userlist = ARGS.users.split(",")

    shadow_file = ShadowFile(ARGS.shadow_file)
    cracker = Cracker(shadow_file, userlist, ARGS.wordlist_file) 
    cracker.crack()

