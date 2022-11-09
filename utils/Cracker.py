from os import geteuid
from sys import stderr
from crypt import crypt

if geteuid() != 0:
    print("ERROR: Password cracker requires root privileges!", file=stderr)
    exit(1)

class Cracker:

    def __init__(self, shadow_file, userlist, wordlistpath):
        self.shadow_file = shadow_file
        self.userlist = userlist
        with open(wordlistpath, "r") as f:
            lines = f.readlines()
            self.wordlist = [line.strip() for line in lines]
    
    def crack(self):
        for entry in self.shadow_file.entries:
            if len(self.userlist) != 0 and entry.username in self.userlist:
                print(f"Attempting to crack user: {entry.username}")
                cryptsalt = entry.salt
                attempts = 0
                for word in self.wordlist:
                    full_hash = crypt(word, cryptsalt)
                    if full_hash == cryptsalt+"$"+entry.password_hash:
                        attempts += 1
                        print(f"Password Found in {attempts} attempts!")
                        print(word)
                        break
                    attempts += 1
            elif len(self.userlist) == 0:
                print(f"Attempting to crack user: {entry.username}")
                cryptsalt = entry.salt
                attempts = 0
                for word in self.wordlist:
                    full_hash = crypt(word, cryptsalt)
                    if full_hash == cryptsalt+"$"+entry.password_hash:
                        attempts += 1
                        print(f"Password Found in {attempts} attempts!")
                        print(word)
                        break
                    attempts += 1
        print("Finished")

