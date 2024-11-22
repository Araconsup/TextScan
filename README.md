# Text Analyzer

Text Analyzer is a command-line application designed to read and analyze text files. It provides various features for text analysis, including counting lines, sentences, words, and occurrences of consecutive words, while allowing users to filter and customize their analysis.

## Features

- Command-line interface for user interaction.
- Specify paths for input files, output files, and ignored words.
- Filter words based on minimum and maximum lengths.
- Count occurrences of consecutive words.
- Output results in JSON format, including:
  - Number of lines, sentences, and words.
  - Occurrences of consecutive words.
  - List of longest words.
  - List of ignored words.
  - Average number of characters in words.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/text-analyzer.git
   ```
2. Navigate to the project directory:
   ```
   cd text-analyzer
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command in your terminal:
```
python src/main.py
```

Follow the prompts to enter the required file paths and analysis parameters.

## Testing

To run the tests, navigate to the `tests` directory and execute:
```
pytest
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.