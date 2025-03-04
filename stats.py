def word_count(txt):
    return len(txt.split())

def char_count(txt):
    char = {}

    for letter in txt:
        lower = letter.lower()
        if lower in char:
            char[lower] += 1
        else:
            char[lower] = 1

    return char
