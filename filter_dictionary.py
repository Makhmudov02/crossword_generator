import json
import os

def open_dictionary(filename):
    """
    Open a JSON dictionary file and return its contents as a dictionary.

    Args:
        filename (str): The name of the JSON file to open.

    Returns:
        dict: The contents of the JSON file as a dictionary.
    """
    try:
        with open(filename) as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' contains invalid JSON.")
        return {}

def create_dictionary(filename, data):
    """
    Create a JSON dictionary file with the given data.

    Args:
        filename (str): The name of the JSON file to create.
        data (dict): The data to write to the JSON file.

    Returns:
        str: The name of the created JSON file.
    """
    try:
        with open(os.path.join('dictionary', filename), 'w') as file:
            json.dump(data, file)
        return filename
    except IOError:
        print(f"Error: Could not write to the file '{filename}'.")
        return None

def filter_words(words, min_length=5, max_length=15, exclude_chars=[' ', '-']):
    """
    Filter words based on length and excluded characters.

    Args:
        words (dict): The dictionary of words to filter.
        min_length (int): The minimum length of words to include.
        max_length (int): The maximum length of words to include.
        exclude_chars (list): A list of characters to exclude from words.

    Returns:
        list: A list of words to remove from the dictionary.
    """
    to_remove = [word for word in words if len(word) > max_length or len(word) < min_length or any(char in word for char in exclude_chars)]
    return to_remove

def clean_definitions(words):
    """
    Clean the definitions of words by removing certain phrases and text.

    Args:
        words (dict): The dictionary of words to clean.

    Returns:
        list: A list of words to remove from the dictionary.
    """
    to_remove = []
    for word in words.keys():
        if word in words[word].lower() or 'See' in words[word] or 'Same as' in words[word]:
            to_remove.append(word)
        if '[R.]' in words[word]:
            index = words[word].index('[R.]')
            words[word] = words[word][:index-1]
        if '[Obs.]' in words[word]:
            index = words[word].index('[Obs.]')
            words[word] = words[word][:index-1]
    return to_remove

def main():
    """
    Main function to filter and clean the dictionary, then create a new filtered dictionary file.
    """
    words = open_dictionary('dictionary/simple_english_dictionary.json')
    if not words:
        return

    to_remove = filter_words(words)
    to_remove.extend(clean_definitions(words))
    to_remove = list(set(to_remove))

    for word in to_remove:
        del words[word]

    create_dictionary('filtered_dictionary.json', words)

if __name__ == "__main__":
    main()
