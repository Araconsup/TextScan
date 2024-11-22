import unittest
from unittest.mock import patch, MagicMock
from src.cli import parse_arguments, handle_file_paths

class TestCLI(unittest.TestCase):

    @patch('src.cli.argparse.ArgumentParser.parse_args')
    def test_parse_arguments(self, mock_parse_args):
        mock_parse_args.return_value = MagicMock(
            input_file='input.txt',
            output_file='output.json',
            ignored_words_file='ignored.txt',
            min_length=3,
            max_length=10,
            consecutive_words=2,
            sort_order='asc'
        )
        args = parse_arguments()
        self.assertEqual(args.input_file, 'input.txt')
        self.assertEqual(args.output_file, 'output.json')
        self.assertEqual(args.ignored_words_file, 'ignored.txt')
        self.assertEqual(args.min_length, 3)
        self.assertEqual(args.max_length, 10)
        self.assertEqual(args.consecutive_words, 2)
        self.assertEqual(args.sort_order, 'asc')

    @patch('src.cli.os.path.exists')
    def test_handle_file_paths_valid(self, mock_exists):
        mock_exists.side_effect = [True, True, True]
        input_file, output_file, ignored_words_file = handle_file_paths('input.txt', 'output.json', 'ignored.txt')
        self.assertEqual(input_file, 'input.txt')
        self.assertEqual(output_file, 'output.json')
        self.assertEqual(ignored_words_file, 'ignored.txt')

    @patch('src.cli.os.path.exists')
    def test_handle_file_paths_invalid(self, mock_exists):
        mock_exists.side_effect = [False, True, True]
        with self.assertRaises(FileNotFoundError):
            handle_file_paths('input.txt', 'output.json', 'ignored.txt')

if __name__ == '__main__':
    unittest.main()