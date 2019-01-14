import requests
from bs4 import BeautifulSoup, Tag
import re

def get_references_ids(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, 'html.parser')
  prs_ref = soup.find_all('a', {'class' : ['issue-link js-issue-link', 'title-link'], 'data-hovercard-type' : 'pull_request'})
  prs_ref_numbers = []
  if len(prs_ref) > 0:
    for ref in prs_ref:
      pr_number = int(re.findall(r'pull/(\d+)', ref.get("href"))[0])
      prs_ref_numbers.append(pr_number)

  return prs_ref_numbers

