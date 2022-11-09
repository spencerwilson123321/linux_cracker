
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
            print(tokens[1])
            if tokens[1] in ["*", "!", "!!", "!*"]:
                self.salt = ""
                self.password_hash = ""
            else:
                pieces = tokens[1].split("$")
                size = len(pieces)
                salt = ""
                for i in range(0, size-1):
                    salt += pieces[i]+"$"
                self.salt = salt[0:len(salt)-1]
                self.password_hash = pieces[size-1]
            self.last_passwd_change = tokens[2]
            self.min_passwd_age = tokens[3]
            self.max_passwd_age = tokens[4]
            self.warning_period = tokens[5]
            self.inactivity_period = tokens[6]
            self.expiration_date = tokens[7]
            self.unused = tokens[8]

