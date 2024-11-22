class TextAnalyzer:
    def __init__(self, input_file, ignored_words_file=None, min_length=0, max_length=float('inf'), consecutive_count=1):
        self.input_file = input_file
        self.ignored_words_file = ignored_words_file
        self.min_length = min_length
        self.max_length = max_length
        self.consecutive_count = consecutive_count
        self.ignored_words = self.load_ignored_words()
        self.text = self.read_file()
        self.analysis_results = {}

    def read_file(self):
        try:
            with open(self.input_file, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: The file {self.input_file} does not exist.")
            return ""

    def load_ignored_words(self):
        if not self.ignored_words_file:
            return set()
        try:
            with open(self.ignored_words_file, 'r', encoding='utf-8') as file:
                return set(word.strip() for word in file.readlines())
        except FileNotFoundError:
            print(f"Error: The ignored words file {self.ignored_words_file} does not exist.")
            return set()

    def analyze(self):
        # Implement analysis logic here
        pass

    def count_lines(self):
        return len(self.text.splitlines())

    def count_sentences(self):
        return self.text.count('.') + self.text.count('!') + self.text.count('?')

    def count_words(self):
        words = self.filter_words(self.text.split())
        return len(words)

    def filter_words(self, words):
        return [word for word in words if self.min_length <= len(word) <= self.max_length and word not in self.ignored_words]

    def count_consecutive_words(self):
        # Implement counting of consecutive words here
        pass

    def generate_output(self):
        # Implement output generation in JSON format here
        pass

    def longest_words(self):
        # Implement logic to find longest words here
        pass

    def average_word_length(self):
        # Implement logic to calculate average word length here
        pass