import json
import os
import sys
from cli import parse_arguments
from analyzer import TextAnalyzer

def main():
    while True:
        args = parse_arguments()
        
        if args.quit:
            print("Exiting the Text Analyzer.")
            break
        
        if not os.path.exists(args.input_file):
            print(f"Error: The input file '{args.input_file}' does not exist.")
            continue
        
        analyzer = TextAnalyzer(args.input_file, args.output_file, args.ignored_words_file)
        
        try:
            analyzer.read_ignored_words()
            analyzer.analyze(min_length=args.min_length, max_length=args.max_length, consecutive_count=args.consecutive_count)
            output = analyzer.generate_output()
            with open(args.output_file, 'w') as outfile:
                json.dump(output, outfile, indent=4)
            print(f"Analysis complete. Results saved to '{args.output_file}'.")
        except Exception as e:
            print(f"An error occurred during analysis: {e}")

if __name__ == "__main__":
    main()