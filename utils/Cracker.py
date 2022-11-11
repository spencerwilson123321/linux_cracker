from os import geteuid
from sys import stderr
from crypt import crypt
from time import perf_counter

if geteuid() != 0:
    print("ERROR: Password cracker requires root privileges!", file=stderr)
    exit(1)


def getAlgorithm(salt: str):
    if "$1$" in salt:
        return "MD5"
    if "$2a$" in salt:
        return "Blowfish"
    if "$2y$" in salt:
        return "Blowfish"
    if "$5$" in salt:
        return "SHA-256"
    if "$6$" in salt:
        return "SHA-512"
    if "$y$" in salt:
        return "yescrypt"
    return "Algorithm not detected"


class Cracker:

    def __init__(self, shadow_file, userlist, wordlistpath):
        self.shadow_file = shadow_file
        self.userlist = userlist
        with open(wordlistpath, "r") as f:
            lines = f.readlines()
            self.wordlist = [line.strip() for line in lines]
    
    def crack(self):
        for entry in self.shadow_file.entries:
            if entry.salt == "":
                continue
            if len(self.userlist) != 0 and entry.username in self.userlist:
                password_found = False
                print(f"Cracking passwords for user: {entry.username}")
                if entry.salt == "":
                    continue
                print(f"Algorithm detected: {getAlgorithm(entry.salt)}")
                cryptsalt = entry.salt
                attempts = 0
                start_time = perf_counter()
                for word in self.wordlist:
                    full_hash = crypt(word, cryptsalt)
                    if full_hash == cryptsalt+"$"+entry.password_hash:
                        stop_time = perf_counter()
                        attempts += 1
                        password_found = True
                        print(f"Password Found in {attempts} attempts!")
                        print(f"Password: {word}")
                        print(f"Duration: {stop_time-start_time:0.4f} seconds")
                        break
                    attempts += 1
                if not password_found:
                    stop_time = perf_counter()
                    print("Password not found!")
                    print(f"Duration: {stop_time-start_time:0.4f} seconds")
            elif len(self.userlist) == 0:
                password_found = False
                print(f"Cracking passwords for user: {entry.username}")
                if entry.salt == "":
                    continue
                print(f"Algorithm detected: {getAlgorithm(entry.salt)}")
                cryptsalt = entry.salt
                attempts = 0
                start_time = perf_counter()
                for word in self.wordlist:
                    full_hash = crypt(word, cryptsalt)
                    if full_hash == cryptsalt+"$"+entry.password_hash:
                        stop_time = perf_counter()
                        attempts += 1
                        password_found = True
                        print(f"Password Found in {attempts} attempts!")
                        print(f"Password: {word}")
                        print(f"Duration: {stop_time-start_time:0.4f} seconds")
                        break
                    attempts += 1
                if not password_found:
                    stop_time = perf_counter()
                    print("Password not found!")
                    print(f"Duration: {stop_time-start_time:0.4f} seconds")

