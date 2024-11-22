import unittest
from src.utils import remove_punctuation, calculate_average, read_ignored_words

class TestUtils(unittest.TestCase):

    def test_remove_punctuation(self):
        self.assertEqual(remove_punctuation("Hello, world!"), "Hello world")
        self.assertEqual(remove_punctuation("Python is great."), "Python is great")
        self.assertEqual(remove_punctuation("No punctuation here"), "No punctuation here")

    def test_calculate_average(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_average([]), 0)
        self.assertEqual(calculate_average([10, 20, 30]), 20.0)

    def test_read_ignored_words(self):
        with open('ignored_words.txt', 'w') as f:
            f.write("the\nand\nis\n")
        self.assertEqual(read_ignored_words('ignored_words.txt'), {'the', 'and', 'is'})
        self.assertEqual(read_ignored_words('non_existent_file.txt'), set())

if __name__ == '__main__':
    unittest.main()