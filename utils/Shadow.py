
AlgorithmTable = {
    "6":"SHA-512",
    "5":"SHA-256",
    "3":"Blowfish",
    "2":"Blowfish",
    "1":"MD5"
}

class ShadowFile:
    """
        A class representing a parsed shadow file.
        Simply contains a list of ShadowFileEntry objects.
    """
    def __init__(self, filepath):
        self.entries = []
        with open(filepath, "r") as f:
            entries = f.readlines()
            for entry in entries:
                self.entries.append(ShadowFileEntry(entry))


class ShadowFileEntry:

    def __init__(self, entry: str = ""):
        # Parse the entry and fill in
        # the instance variables.
        if entry == "":
            self.username = ""
            self.algorithm = ""
            self.salt = ""
            self.password_hash = ""
            self.last_passwd_change = ""
            self.min_passwd_age = ""
            self.max_passwd_age = ""
            self.warning_period = ""
            self.inactivity_period = ""
            self.expiration_date = ""
            self.unused = ""
        else:
            tokens = entry.split(":")
            self.username = tokens[0]
            if tokens[1] in ["*", "!", "!!", "!*"]:
                self.algorithm = ""
                self.salt = ""
                self.password_hash = ""
            else:
                extra, algorithm, extra2, salt, password_hash = tokens[1].split("$")
                print(tokens[1].split("$"))
                self.algorithm = algorithm
                self.salt = salt
                self.password_hash = password_hash
            self.last_passwd_change = tokens[2]
            self.min_passwd_age = tokens[3]
            self.max_passwd_age = tokens[4]
            self.warning_period = tokens[5]
            self.inactivity_period = tokens[6]
            self.expiration_date = tokens[7]
            self.unused = tokens[8]

