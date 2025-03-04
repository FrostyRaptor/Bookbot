import sys
from stats import char_count, word_count
from sort import sort_dict

def print_char_report(txt):
    dict = char_count(txt)
    lst = sort_dict(dict)

    print(f"--- Begin report of {sys.argv[1]} ---")
    print(f"{word_count(txt)} words found in the document\n")

    for item in lst:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("\n--- End Report ---")

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    with open(sys.argv[1]) as txt:
        user_txt = txt.read()

    print_char_report(user_txt)

main()