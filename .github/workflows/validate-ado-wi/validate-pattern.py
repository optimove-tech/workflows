import re
import ast
import argparse
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_args():
    parser = argparse.ArgumentParser(
        description='Parameters to validate pattern'
    )

    parser.add_argument('-checklist', dest='checklist', type=str,
                        help='Specify checklist to parse. Example: [PR_BODY, PR_TITLE]',
                        required=True)
    
    args = parser.parse_args()
    checklist = ast.literal_eval(args.checklist)
    return checklist

def check_for_pattern(strings):
    pattern = r"AB#\d+"
    check_confirmed = [string for string in strings if re.search(pattern, string)]
    return check_confirmed

def validate_check(check_confirmed):
    if check_confirmed:
        logging.info(f"Found linked working item: {check_confirmed}...")
        return

    logging.error("No linked working item found...")
    raise ValueError("No linked working item found.")

def main(checklist):
    check_result = check_for_pattern(checklist)
    validate_check(check_result)

if __name__ == "__main__":
    checklist = parse_args()
    main(checklist=checklist)
