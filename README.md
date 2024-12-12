# crossword_generator
Tool to generate crosswords.

## How to Use the Tool

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/crossword_generator.git
    cd crossword_generator
    ```

2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run the tool:
    ```
    python main.py
    ```

## Examples

Here are some examples of how to use the tool:

- To generate a crossword with the default settings:
    ```
    python main.py
    ```

- To generate a crossword with a custom keyword and size:
    ```
    python main.py --keyword "example" --size 10
    ```

## Options and Features

- `--keyword`: The keyword to be used in the crossword (default: "crossword").
- `--size`: The size of the crossword grid (default: 15).

## File Structure

- `filter_dictionary.py`: Contains functions to open, create, filter, and clean the dictionary.
- `main.py`: Contains the `Crossword` class and the main function to generate the crossword.
- `dictionary/filtered_dictionary.json`: The filtered dictionary used by the tool.
- `dictionary/simple_english_dictionary.json`: The original dictionary used by the tool.
- `tests/test_filter_dictionary.py`: Unit tests for the functions in `filter_dictionary.py`.
- `tests/test_main.py`: Unit tests for the functions in `main.py`.

## Changelog

### v1.0.0
- Initial release
