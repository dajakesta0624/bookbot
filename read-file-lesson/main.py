import sys
from stats import get_num_words, count_characters, sort_character_counts  # Import the functions

def get_book_text(path):
    """Reads the contents of a file and returns it as a string."""
    with open(path) as f:
        return f.read()

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # Take the book path from command-line argument
    text = get_book_text(book_path)  # Read the contents of the book

    # Word count
    num_words = get_num_words(text)

    # Character count
    char_count = count_characters(text)

    # Sort character counts
    sorted_char_counts = sort_character_counts(char_count)

    # Printing the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    # Display results for 'e' and 't'
    for entry in sorted_char_counts:
        if entry["char"] == 'e' or entry["char"] == 't':
            print(f"{entry['char']}: {entry['num']}")

if __name__ == "__main__":
    main()

