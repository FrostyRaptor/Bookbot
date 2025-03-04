from stats import char_count, word_count
from sort import sort_dict

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