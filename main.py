from stats import count_words, count_character, sorted_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.ext(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
# Open books and read in string

def main():
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    char_count = count_character(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    characters_list = sorted_dict(char_count)
    for item in characters_list:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

