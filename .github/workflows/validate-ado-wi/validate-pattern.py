import re
import argparse
import sys  # Import the sys module

def check_for_pattern(strings):
    pattern = r"AB#\d+"
    matches = [string for string in strings if re.search(pattern, string)]
    return matches

def main():
    parser = argparse.ArgumentParser(description="Check for AB# pattern in a list of strings.")
    parser.add_argument('strings', nargs='+', help='List of strings to check')
    args = parser.parse_args()

    matches = check_for_pattern(args.strings)
    if matches:
        print("Found matches:", matches)
    else:
        print("No matches found.")
        sys.exit(1)  # Exit with code 1 if no matches are found

if __name__ == "__main__":
    main()
