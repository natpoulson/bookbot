import sys
from stats import get_num_chars, get_num_words, create_sorted_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>");
        sys.exit(1)
    book_path = sys.argv[1]
    source = get_book_text(book_path)
    wordcount = get_num_words(source)
    sorted_dict = create_sorted_dictionary(get_num_chars(source))
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_path}...')
    print("----------- Word Count ----------")
    print(f'Found {wordcount} total words')
    print("--------- Character Count -------")
    for item in sorted_dict:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END ===============")

main()
