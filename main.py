def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_contents = f.read()
    return file_contents

def main():
    # Update the path to include the books folder
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)

if __name__ == '__main__':
    main()
