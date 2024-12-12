import unittest
from filter_dictionary import open_dictionary, create_dictionary, filter_words, clean_definitions

class TestFilterDictionary(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            "apple": "A fruit that is red or green.",
            "banana": "A long yellow fruit.",
            "cherry": "A small red fruit.",
            "date": "A sweet fruit from the date palm.",
            "elderberry": "A small dark purple fruit.",
            "fig": "A sweet fruit with a unique texture.",
            "grape": "A small round fruit that can be red, green, or purple.",
            "honeydew": "A type of melon with sweet green flesh.",
            "kiwi": "A small brown fruit with green flesh.",
            "lemon": "A sour yellow fruit.",
            "mango": "A tropical fruit with sweet orange flesh.",
            "nectarine": "A smooth-skinned fruit similar to a peach.",
            "orange": "A citrus fruit with a tough skin.",
            "papaya": "A tropical fruit with sweet orange flesh.",
            "quince": "A yellow fruit that is similar to a pear.",
            "raspberry": "A small red fruit with a sweet-tart flavor.",
            "strawberry": "A red fruit with a sweet flavor.",
            "tangerine": "A small citrus fruit with a sweet flavor.",
            "ugli": "A hybrid citrus fruit with a rough, wrinkled skin.",
            "vanilla": "A flavoring derived from orchids of the genus Vanilla.",
            "watermelon": "A large fruit with a green rind and sweet red flesh.",
            "xigua": "A type of watermelon with a green rind and sweet red flesh.",
            "yellowfruit": "A fictional fruit for testing purposes.",
            "zucchini": "A type of summer squash with a mild flavor."
        }

    def test_open_dictionary(self):
        data = open_dictionary('dictionary/simple_english_dictionary.json')
        self.assertIsInstance(data, dict)

    def test_create_dictionary(self):
        filename = create_dictionary('test_dictionary.json', self.sample_data)
        self.assertEqual(filename, 'test_dictionary.json')

    def test_filter_words(self):
        filtered_words = filter_words(self.sample_data, min_length=5, max_length=10, exclude_chars=[' ', '-'])
        expected_words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'lemon', 'mango', 'orange', 'papaya', 'quince', 'ugli', 'vanilla', 'xigua', 'zucchini']
        self.assertEqual(filtered_words, expected_words)

    def test_clean_definitions(self):
        self.sample_data['apple'] = "A fruit that is red or green. See also: fruit."
        self.sample_data['banana'] = "A long yellow fruit. Same as: plantain."
        self.sample_data['cherry'] = "A small red fruit. [R.]"
        self.sample_data['date'] = "A sweet fruit from the date palm. [Obs.]"
        cleaned_words = clean_definitions(self.sample_data)
        expected_words = ['apple', 'banana', 'cherry', 'date']
        self.assertEqual(cleaned_words, expected_words)
        self.assertEqual(self.sample_data['cherry'], "A small red fruit.")
        self.assertEqual(self.sample_data['date'], "A sweet fruit from the date palm.")

if __name__ == '__main__':
    unittest.main()
