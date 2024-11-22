def remove_punctuation(text):
    import string
    return text.translate(str.maketrans('', '', string.punctuation))

def calculate_average_word_length(words):
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

def read_ignored_words(file_path):
    try:
        with open(file_path, 'r') as file:
            return {line.strip() for line in file if line.strip()}
    except FileNotFoundError:
        return set()  # Return an empty set if the file is not found

def filter_words_by_length(words, min_length=0, max_length=float('inf')):
    return [word for word in words if min_length <= len(word) <= max_length]