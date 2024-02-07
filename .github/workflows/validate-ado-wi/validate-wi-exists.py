
import re
import requests
import argparse
import sys 

def extract_and_verify_work_items(strings, organization, project, pat):
    pattern = r"AB#(\d+)"
    headers = {
        'Content-Type': 'application/json'
    }

    for string in strings:
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

def main():
    parser = argparse.ArgumentParser(description="Extract AB# pattern strings and verify with ADO API.")
    parser.add_argument('strings', nargs='+', help='List of strings to check')
    parser.add_argument('--org', required=True, help='Azure DevOps organization')
    parser.add_argument('--project', required=True, help='Azure DevOps project')
    parser.add_argument('--pat', required=True, help='Personal Access Token for Azure DevOps API')
    args = parser.parse_args()

    extract_and_verify_work_items(args.strings, args.org, args.project, args.pat)

if __name__ == "__main__":
    main()
