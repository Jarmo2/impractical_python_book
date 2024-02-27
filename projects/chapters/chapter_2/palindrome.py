"""Find palindromes (letter in palingrams) in a dictionary file."""

import load_dictionary

FILE_LOCATION = '../../../12dicts-6.0.2/International/2of4brif.txt'

WORDS = load_dictionary.load(FILE_LOCATION)

def palindrome_checker() -> list[str]:
    """Find palindromes in dictionary file."""
    palindromes = []
    for word in WORDS:
        if len(word) > 1 and word[::-1] in WORDS:
            palindromes.append(word)
    return palindromes


result = palindrome_checker()

print(f"\nNumber of Palindromes found: {len(result)}")
print(*result, sep='\n')