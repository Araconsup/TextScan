import unittest
from src.analyzer import TextAnalyzer

class TestTextAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = TextAnalyzer()

    def test_count_lines(self):
        result = self.analyzer.count_lines("test_file.txt")
        self.assertEqual(result, expected_line_count)

    def test_count_sentences(self):
        result = self.analyzer.count_sentences("test_file.txt")
        self.assertEqual(result, expected_sentence_count)

    def test_count_words(self):
        result = self.analyzer.count_words("test_file.txt")
        self.assertEqual(result, expected_word_count)

    def test_filter_words_length(self):
        result = self.analyzer.filter_words_length(["word", "another"], min_length=3, max_length=5)
        self.assertEqual(result, ["word"])

    def test_count_consecutive_words(self):
        result = self.analyzer.count_consecutive_words("test_file.txt", n=2)
        self.assertEqual(result, expected_consecutive_word_count)

    def test_generate_output(self):
        output = self.analyzer.generate_output("test_file.txt")
        self.assertIn("lines", output)
        self.assertIn("sentences", output)
        self.assertIn("words", output)
        self.assertIn("consecutive_word_counts", output)

if __name__ == '__main__':
    unittest.main()