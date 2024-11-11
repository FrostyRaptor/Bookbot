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
def sort_on(d):
    return d["num"]

def sort_dict(dict):
    sorted_lst = []

    for char in dict:
        sorted_lst.append({"char": char, "num": dict[char]})
 
    sorted_lst.sort(reverse=True, key=sort_on)
    return sorted_lst

def print_char_report(txt):
    dict = char_count(txt)
    lst = sort_dict(dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count(txt)} words found in the document\n")

    for item in lst:
        if item["char"].isalpha():
            print(f"The {item["char"]} character was found {item["num"]} times")

    print("\n--- End Report ---")

def main():

    with open("books/frankenstein.txt") as txt:
        frankenstein_txt = txt.read()

    print_char_report(frankenstein_txt)

main()