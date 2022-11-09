

class PasswdFile:
    """
    """
    def __init__(self, filepath):
        self.entries = []
        with open(filepath, "r") as f:
            entries = f.readlines()
            for entry in entries:
                self.entries.append(PasswdFileEntry(entry))


class PasswdFileEntry:

    def __init__(self, entry: str = ""):
        # Parse the entry and fill in
        # the instance variables.
        if entry == "":
            self.username = ""
            self.password = ""
            self.uid = ""
            self.gid = ""
            self.info = ""
            self.home = ""
            self.shell = ""
        else:
            tokens = entry.split(":")
            self.username = tokens[0]
            self.password = tokens[1]
            self.uid = tokens[2]
            self.gid = tokens[3]
            self.info = tokens[4]
            self.home = tokens[5]
            self.shell = tokens[6]

