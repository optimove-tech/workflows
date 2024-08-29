import re
import argparse
import sys  # Import the sys module

def check_for_pattern(strings):
    pattern = r"AB#\d+"
    check_confirmed = [string for string in strings if re.search(pattern, string)]
    return check_confirmed

def main():
    parser = argparse.ArgumentParser(description="Check for AB# pattern in a list of strings.")
    parser.add_argument('strings', nargs='+', help='List of strings to check')
    args = parser.parse_args()

    check_confirmed = check_for_pattern(args.strings)
    if check_confirmed:
        print("Found check_confirmed:", check_confirmed)
    else:
        print("No check_confirmed found.")
        sys.exit(1)  # Exit with code 1 if no check_confirmed are found

if __name__ == "__main__":
    main()
