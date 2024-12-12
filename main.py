from filter_dictionary import open_dictionary
import random


class Crossword:
    """
    A class to represent a crossword puzzle.

    Attributes:
        keyword (str): The keyword to be used in the crossword.
        words (dict): The dictionary of words and their definitions.
        size (int): The size of the crossword grid.
        is_keyword_set (bool): Flag to indicate if the keyword should be set in the crossword.
        crossword (list): The crossword grid.
        questions (dict): The dictionary of questions for the crossword.
    """
    def __init__(self, keyword='crossword', size=15, set_keyword=True):
        """
        Initialize the Crossword object.

        Args:
            keyword (str): The keyword to be used in the crossword.
            size (int): The size of the crossword grid.
            set_keyword (bool): Flag to indicate if the keyword should be set in the crossword.
        """
        self.keyword = keyword
        self.words = open_dictionary('dictionary/filtered_dictionary.json')
        self.size = size
        self.is_keyword_set = set_keyword
        self.crossword = []
        self.questions = {}
        
    def __str__(self):
        """
        Return a string representation of the crossword grid.

        Returns:
            str: The crossword grid as a string.
        """
        crossword = '\n'.join([''.join(row) for row in self.crossword])
        return crossword
    
    def set_keyword(self):
        """
        Set the keyword in the middle column of the crossword grid.

        Returns:
            list: The updated crossword grid.
        """
        middle = self.size // 2
        for i, letter in enumerate(self.keyword):
            self.crossword[i][middle] = letter
        return self.crossword
    
    def create_crossword(self):
        """
        Create the crossword grid and set the keyword if required.

        Returns:
            list: The created crossword grid.
        """
        self.crossword = [['*' for _ in range(self.size)] for _ in range(len(self.keyword))]
        if self.is_keyword_set:
            self.crossword = self.set_keyword()
        return self.crossword
    
    def generate_questions(self):
        """
        Generate questions for the crossword based on the keyword.

        Returns:
            None
        """
        for letter in self.keyword:
            while True:
                answer, question = random.choice(list(self.words.items()))
                if letter in answer and answer.index(letter) > 0  and answer.index(letter) < len(answer)-2 and answer not in self.questions.keys():
                    self.questions[answer] = question
                    break
        print(self.questions)
                
if __name__ == "__main__":
    try:
        crossword = Crossword()
        crossword.create_crossword()
        crossword.generate_questions()
        print(crossword)
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
