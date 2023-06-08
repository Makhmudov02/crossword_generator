from filter_dictionary import open_dictionary
import random


class Crossword:
    def __init__(self, keyword='crossword', size=15, set_keyword=True):
        self.keyword = keyword
        self.words = open_dictionary('dictionary/filtered_dictionary.json')
        self.size = size
        self.is_keyword_set = set_keyword
        self.crossword = []
        self.questions = {}
        
    def __str__(self):
        crossword = '\n'.join([''.join(row) for row in self.crossword])
        return crossword
    
    def set_keyword(self):
        middle = self.size // 2
        for i, letter in enumerate(self.keyword):
            self.crossword[i][middle] = letter
        return self.crossword
    
    def create_crossword(self):
        self.crossword = [['*' for _ in range(self.size)] for _ in range(len(self.keyword))]
        if self.is_keyword_set:
            self.crossword = self.set_keyword()
        return crossword
    
    def generate_questions(self):
        for letter in self.keyword:
            while True:
                answer, question = random.choice(list(self.words.items()))
                if letter in answer and answer.index(letter) > 0  and answer.index(letter) < len(answer)-2 and answer not in self.questions.keys():
                    self.questions[answer] = question
                    break
        print(self.questions)
                
if __name__ == "__main__":
    crossword = Crossword()
    crossword.create_crossword()
    crossword.generate_questions()
    print(crossword)
    