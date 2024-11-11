def main():

    with open("books/frankenstein.txt") as txt:
        frankenstein_txt = txt.read()

    print(frankenstein_txt)

main()