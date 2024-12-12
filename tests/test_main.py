import unittest
from main import Crossword

class TestCrossword(unittest.TestCase):

    def setUp(self):
        self.crossword = Crossword()

    def test_create_crossword(self):
        crossword_grid = self.crossword.create_crossword()
        self.assertEqual(len(crossword_grid), len(self.crossword.keyword))
        self.assertEqual(len(crossword_grid[0]), self.crossword.size)

    def test_set_keyword(self):
        self.crossword.create_crossword()
        crossword_grid = self.crossword.set_keyword()
        middle = self.crossword.size // 2
        for i, letter in enumerate(self.crossword.keyword):
            self.assertEqual(crossword_grid[i][middle], letter)

    def test_generate_questions(self):
        self.crossword.generate_questions()
        self.assertEqual(len(self.crossword.questions), len(self.crossword.keyword))
        for answer in self.crossword.questions.keys():
            self.assertIn(answer, self.crossword.words)

if __name__ == '__main__':
    unittest.main()