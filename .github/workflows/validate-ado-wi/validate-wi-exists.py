
import re
import ast
import argparse
import sys
import requests

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
    
    parser.add_argument('-pat', dest='pat', type=str,
                        help='Private Access Token for auth',
                        required=True)
    
    args = parser.parse_args()
    checklist = ast.literal_eval(args.checklist)
    organization = args.organization
    project = args.project
    pat = args.pat
    
    return checklist, organization, project, pat

def extract_and_verify_work_items(checklist, organization, project, pat):
    pattern = r"AB#(\d+)"
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
                print(f"Work item AB#{work_item_id} exists.")
            else:
                print(f"Work item AB#{work_item_id} does not exist or access denied.")
                print(response.status_code)
                sys.exit(1)

def main(checklist, organization, project, pat):
    extract_and_verify_work_items(checklist, organization, project, pat)

if __name__ == "__main__":
    _checklist, _organization, _project, _pat = parse_args()
    main(checklist=_checklist, organization=_organization, project=_project, pat=_pat)
