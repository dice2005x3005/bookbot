from stats import get_num_words, get_counts, sorted_counts
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text():
    with open(sys.argv[1], encoding="utf-8") as f:
        content = f.read()
        return content
print('============ BOOKBOT ============')
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")
print(get_num_words(get_book_text()))
print("--------- Character Count -------")
x = sorted_counts(get_counts(get_book_text()))
for i in x:
    print(f'{i["char"]}: {i["num"]}')


