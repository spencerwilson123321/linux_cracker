
class WordListProcessor:

    def __init__(self):
        pass

    def chunkify(self, wordlist_file: str, num: int) -> list:
        """
            Takes a list of words, and breaks them up into 'num' similarly sized lists.
        """
        chunk_list = []
        lines = None
        with open(wordlist_file, "r") as f:
            lines = f.readlines()
            lines = map(lambda x : x.strip("\n"), lines)
            lines = list(lines)
        if lines is not None:
            if num == 1:
                return [lines]
            num_leftover = len(lines) % num
            step_size = int(len(lines)/num)
            num_lines = len(lines)
            # Split the wordlist into num chunks.
            if num_leftover != 0:
                for i in range(0, num_lines-step_size, step_size):
                    chunk_list.append(lines[i:i+step_size])
                chunk_list[len(chunk_list)-1] = chunk_list[len(chunk_list)-1] + lines[num_lines-num_leftover:]
            else:
                for i in range(0, num_lines, step_size):
                    chunk_list.append(lines[i:i+step_size])
            return chunk_list
        else: # File read failed.
            return []
