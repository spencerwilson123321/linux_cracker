import argparse
import os
from sys import stderr
from multiprocessing import Process

from utils.Cracker import Cracker
from utils.Shadow import ShadowFile
from utils.WordListProcessor import WordListProcessor


if __name__ == "__main__":

    # Parse Command Line arguments.
    PARSER = argparse.ArgumentParser("./cracker.py")
    PARSER.add_argument("shadow_file", help="Path to the shadow file.")
    PARSER.add_argument("wordlist_file", help="Path to the wordlist file.")
    PARSER.add_argument("-u", "--users", dest="users", help="A comma-separated list of usernames, only the given users will be targeted.", required=False)
    PARSER.add_argument("-t", "--threads", dest="threads", help="The number of threads to use for cracking the passwords. Default 1.", default="1")
    ARGS = PARSER.parse_args()
    
    # ----------------------------- ERROR CHECKING ------------------------
    if not os.path.isfile(ARGS.wordlist_file):
        print(f"ERROR: File not found '{ARGS.wordlist_file}'", file=stderr)
        exit(1)

    if not os.path.isfile(ARGS.shadow_file):
        print(f"ERROR: File not found '{ARGS.shadow_file}'", file=stderr)
        exit(1)

    try:
        temp = int(ARGS.threads)
    except ValueError:
        print(f"Expected integer for optional argument -t\nReceived {ARGS.threads} instead.", file=stderr)
        exit(1)
    if temp < 1:
        print(f"Number of threads cannot be below 1.", file=stderr)
        exit(1)

    # ------------------------------ DATA -----------------------------------
    if ARGS.users is None:
        USERLIST = []
    else:
        USERLIST = ARGS.users.split(",")
    SHADOW_FILE = ShadowFile(ARGS.shadow_file)
    PROCESSOR = WordListProcessor()
    THREADS = []
    CRACKER_INSTANCES = []
    NUM_THREADS = int(ARGS.threads)

    # Split the wordlist into NUM_THREADS chunks
    wordlist_chunks = PROCESSOR.chunkify(ARGS.wordlist_file, NUM_THREADS)

    # Make a Cracker object for each thread.
    print("Starting threads...")
    results = []
    for i in range(0, NUM_THREADS):
        CRACKER_INSTANCES.append(Cracker(SHADOW_FILE, USERLIST, wordlist_chunks[i]))
        THREADS.append(Process(target=CRACKER_INSTANCES[i].crack))
    for thread in THREADS:
        thread.start()
    for thread in THREADS:
        thread.join()

