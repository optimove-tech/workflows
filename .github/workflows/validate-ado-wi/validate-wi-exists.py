
import re
import ast
import argparse
import logging
import sys
import requests
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_args():
    parser = argparse.ArgumentParser(
        description='Parameters to validate pattern'
    )

    parser.add_argument('-checklist', dest='checklist', type=str,
                        help='Specify checklist to parse. Example: [PR_BODY, PR_TITLE]',
                        required=True)

    parser.add_argument('-organization', dest='organization', type=str,
                        help='Azure Organization name. Example: mobius',
                        required=True)
    
    parser.add_argument('-project', dest='project', type=str,
                        help='Azure Project name. Example: Backstage',
                        required=True)
    
    args = parser.parse_args()
    checklist = ast.literal_eval(args.checklist)
    organization = args.organization
    project = args.project
    
    return checklist, organization, project

def extract_and_verify_work_items(checklist, organization, project):
    pattern = r"AB#(\d+)"
    pat = os.getenv('ADO_PAT')
    headers = {
        'Content-Type': 'application/json'
    }

    for string in checklist:
        for match in re.finditer(pattern, string):
            work_item_id = match.group(1)
            url = f"https://dev.azure.com/{organization}/{project}/_apis/wit/workitems/{work_item_id}?api-version=6.0"
            print(url)
            response  = requests.get(url, headers=headers, auth=('', pat))
            if response.status_code == 200:
                logging.info(f"Work item AB#{work_item_id} exists.")
                return
            
            logging.error(f"Work item AB#{work_item_id} does not exist or access denied.")
            logging.error(response.status_code)
            raise ValueError("Work item AB#{work_item_id} does not exist or access denied.")

def main(checklist, organization, project):
    extract_and_verify_work_items(checklist, organization, project)

if __name__ == "__main__":
    _checklist, _organization, _project = parse_args()
    main(checklist=_checklist, organization=_organization, project=_project)
