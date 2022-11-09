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
                print(f"Cracking passwords for user: {entry.username}")
                if entry.salt == "":
                    print(f"Cannot crack password for user: {entry.username}\n")
                    continue
                cryptsalt = entry.salt
                attempts = 0
                password_found = False
                for word in self.wordlist:
                    full_hash = crypt(word, cryptsalt)
                    if full_hash == cryptsalt+"$"+entry.password_hash:
                        attempts += 1
                        password_found = True
                        print(f"Password Found in {attempts} attempts!")
                        print(f"Password: {word}")
                        break
                    attempts += 1
                if not password_found:
                    print(f"No passwords found for user: {entry.username}")
                    continue
                print("")
            elif len(self.userlist) == 0:
                print(f"Cracking passwords for user: {entry.username}\n")
                if entry.salt == "":
                    print(f"Cannot crack password for user: {entry.username}")
                cryptsalt = entry.salt
                attempts = 0
                password_found = False
                for word in self.wordlist:
                    full_hash = crypt(word, cryptsalt)
                    if full_hash == cryptsalt+"$"+entry.password_hash:
                        attempts += 1
                        password_found = True
                        print(f"Password Found in {attempts} attempts!")
                        print(f"Password: {word}")
                        break
                    attempts += 1
                if not password_found:
                    print(f"No passwords found for user: {entry.username}")
                print("")
        print("Finished")

