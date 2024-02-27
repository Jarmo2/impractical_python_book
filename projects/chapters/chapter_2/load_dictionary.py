"""Load a txt file as a list.

Arguments:
- text file name (and directory path, if needed)

Exceptions:
- IOError if file cannot be opened

Return:
- A list of all words in a text file in lower case

Requires-import sys

"""
import sys

def load(file: str) -> list[str]:
    """Open a txt file & return a list of lowercase strings."""
    try:
        with open(file, "r") as imported_file:
            loaded_txt = imported_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print(f"{e}\nError opening {file}. Terminating program.", file=sys.stderr)
        sys.exit(1)


