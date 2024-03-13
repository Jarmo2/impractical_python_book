"""find all word-pair palingrams in a dictionary file."""
import load_dictionary

DICTIONARY_LOCATION = '../../../12dicts/International/2of4brif.txt'


def find_palingrams():
    """Find dictionary palingrams"""
    palingrams = []
    words = set(load_dictionary.load(DICTIONARY_LOCATION))
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end - i:] in words:
                    palingrams.append((word, rev_word[end -i :]))
                if word[:i] == rev_word[end - i:] and rev_word[:end -i] in words:
                    palingrams.append((rev_word[:end-i], word))
    return palingrams
