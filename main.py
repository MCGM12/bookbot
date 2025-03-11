import sys
from stats import get_num_words
from stats import count_characters
from stats import get_book_text


def main():
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(file_path)
    characters = count_characters(file_path)

    # print(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in characters.items():
        print (f"{key}: {value}")
    print("============= END ===============")
    return None

main()

