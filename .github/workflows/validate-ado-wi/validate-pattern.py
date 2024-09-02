import re
import ast
import argparse
import sys  # Import the sys module

def parse_args():
    parser = argparse.ArgumentParser(
        description='Parameters to validate pattern',
        usage='-checklist [PR_TITLE, PR_BODY]')

    parser.add_argument('-checklist', dest='checklist', type=str,
                        help='Specify checklist to parse'
                             'Example: PR_BODY',
                        required=True)
    
    args = parser.parse_args()
    checklist = ast.literal_eval(args.checklist)

    return (checklist)

def check_for_pattern(strings):
    pattern = r"AB#\d+"
    check_confirmed = [string for string in strings if re.search(pattern, string)]
    return check_confirmed

def validate_check(check_confirmed):
    if check_confirmed:
        print("Found linked working item:", check_confirmed)
    else:
        print("No linked working item found.")
        sys.exit(1)

def main(checklist):
    check_result = check_for_pattern(checklist)
    validate_check(check_result)

if __name__ == "__main__":
    _checklist = parse_args()
    main(checklist=_checklist)