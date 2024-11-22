import argparse
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description='Text Analyzer CLI')
    parser.add_argument('--input', type=str, required=True, help='Path to the input text file')
    parser.add_argument('--output', type=str, required=True, help='Path to the output JSON file')
    parser.add_argument('--ignored', type=str, required=True, help='Path to the file containing ignored words')
    parser.add_argument('--min_length', type=int, default=0, help='Minimum word length to consider')
    parser.add_argument('--max_length', type=int, default=float('inf'), help='Maximum word length to consider')
    parser.add_argument('--consecutive', type=int, default=1, help='Number of consecutive words to count')
    parser.add_argument('--sort', type=str, choices=['asc', 'desc'], help='Sort output in ascending or descending order')

    return parser.parse_args()

def validate_file_path(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

def main():
    args = parse_arguments()
    
    try:
        validate_file_path(args.input)
        validate_file_path(args.output)
        validate_file_path(args.ignored)
        
        # Further processing would go here, such as calling the TextAnalyzer class methods

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()