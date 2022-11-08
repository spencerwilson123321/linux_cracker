from utils.Cracker import Cracker
from utils.ShadowParser import ShadowParser

if __name__ == "__main__":
    c = Cracker()
    parser = ShadowParser()
    parser.parse("/etc/shadow")

