from stats import get_num_words, sort_chars
import sys

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    count = get_num_words(sys.argv[1])
    print("============ BOOKBOT ============\n"
    "Analyzing book found at books/frankenstein.txt...\n"
    "----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    letters = sort_chars(sys.argv[1])
    for letter in letters:
        print(f"{letter["char"]}: {letter["num"]}")

main()
