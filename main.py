def get_book_text(filepath):
    """Reads the contents of a file and returns it as a string."""
    with open(filepath, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    """Main function to print the contents of Frankenstein."""
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)  # This outputs the content, which can be redirected

if __name__ == '__main__':
    main()

