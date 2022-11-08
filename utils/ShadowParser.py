
class ShadowParser:

    def __init__(self):
        pass

    def parse(self, filepath):
        print(f"Parsing Shadow File: {filepath}")
        with open("/etc/shadow", "r") as f:
            print(f.read())

class ShadowFile:
    """
        A class representing a parsed shadow file.
        Simply contains a list of ShadowFileEntry objects.
    """
    def __init__(self):
        pass


class ShadowFileEntry:

    def __init__(self, entry: str = ""):
        # Parse the entry and fill in
        # the instance variables.
        if entry == "":
            pass
        else:
            pass

