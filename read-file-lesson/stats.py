# stats.py

def get_num_words(text):
    """Counts the number of words in the given text."""
    words = text.split()  # Split the text into a list of words
    return len(words)     # Return the number of words

def count_characters(text):
    """Counts the occurrences of each character in the given text."""
    char_count = {}  # Initialize an empty dictionary

    # Convert text to lowercase and iterate through each character
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1  # Increment count if character exists
        else:
            char_count[char] = 1   # Initialize count if character is new

    return char_count  # Return the dictionary of character counts

def sort_character_counts(char_count):
    """Sorts the character counts and returns a list of dictionaries."""
    sorted_counts = []

    # Convert dictionary to list of dictionaries
    for char, count in char_count.items():
        if char.isalpha():  # Skip non-alphabetical characters
            sorted_counts.append({"char": char, "num": count})

    # Sort the list by the 'num' key in descending order
    sorted_counts.sort(key=lambda x: x["num"], reverse=True)

    return sorted_counts  # Return the sorted list

