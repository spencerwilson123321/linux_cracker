from utils.Cracker import Cracker
from utils.Shadow import ShadowFile, ShadowFileEntry
from utils.Passwd import PasswdFile, PasswdFileEntry

if __name__ == "__main__":
    c = Cracker()
    shadow_file = ShadowFile("shadow")
    passwd_file = PasswdFile("passwd") 
    for entry in passwd_file.entries:
        print(entry.username)
        print(entry.password)
        print()





