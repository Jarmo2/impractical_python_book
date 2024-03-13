"""find all word-pair palingrams in a dictionary file."""
import load_dictionary

DICTIONARY_LOCATION = '../../../12dicts/International/2of4brif.txt'


def find_palingrams() -> list[tuple[str]]:
    """Find dictionary word-pair palingrams"""
    words_to_check = load_dictionary.load(DICTIONARY_LOCATION)
    #words_to_check = ["level", "noon", "racecar", "kayak", "refer", "madam"]
    palingrams = []
    for word in words_to_check:
        last_char = len(word)
        rev_word = word[::-1]
        if last_char > 1:
            for i in range(last_char):
                if word[i:] == rev_word[:last_char - i] and rev_word[last_char - i:] in words_to_check:
                    palingrams.append((word, rev_word[last_char-i:]))
                if word[:i] == rev_word[last_char-i:] and rev_word[:last_char - i] in words_to_check:
                    palingrams.append((rev_word[:last_char - i], word))
    return palingrams

palingrams = find_palingrams()

palingrams.sort()


print(f"\nNumber of palingrams = {len(palingrams)}\n")
for first, second in palingrams:
    print(f"{first}, {second}")


